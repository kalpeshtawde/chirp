import os
import logging
import requests
from datetime import timedelta, datetime
from time import sleep

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.utils import timezone

from backend.models import TelegramAccount, UserTweet, Messages

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class TelegramBot:

    def __init__(self):
        self.token = os.environ.get("TELEGRAM_TOKEN")

    def _create_user(self, message):
        username = f"{message['from']['first_name']}_" \
                   f"{message['from']['last_name']}_" \
                   f"{message['from']['id']}"

        log.info(f"Creating account {username}")
        try:
            user, created = User.objects.get_or_create(
                username=username.lower(),
                first_name=message['from']['first_name'],
                last_name=message['from']['last_name'],
            )
            telegram_account = TelegramAccount(
                user=user,
                telegram_user_id=message['from']['id'],
                is_bot=message['from']['is_bot'],
                chat_id=message['chat']['id'],

            )
            telegram_account.save()
        except Exception as error:
            log.info(
                f"Creating account failed for {username=} "
                f"with {error=}"
            )

    def user_updates(self):
        log.info("Fetching user updates")
        try:
            update_id = 1
            msg = Messages.objects.values('update_id').order_by(
                '-update_id').first()
            if msg:
                update_id = msg.get('update_id')
            url = f"https://api.telegram.org/bot" \
                  f"{self.token}/getUpdates?offset={update_id}"
            response = requests.get(url).json()
            if response['ok']:
                for result in response['result']:
                    message = result['message']
                    account = TelegramAccount.objects.filter(
                        telegram_user_id=message['from']['id'],
                    )
                    if account.count() == 0:
                        self._create_user(message)
                    try:
                        msg_obj, created = Messages.objects.get_or_create(
                            update_id=result["update_id"],
                            defaults={
                                "user": account[0].user,
                                "message_id": message["message_id"],
                                "date": datetime.fromtimestamp(
                                    int(message["date"])),
                                "text": message["text"],
                            }
                        )
                        if created:
                            log.info(f"Received new message from user "
                                     f"{account[0].user}")
                    except Exception as error:
                        log.error(f"Storing message failed {error=}")
            else:
                log.error(f"Getting user updates failed {response}")
        except Exception as error:
            log.error(f"Getting user updates failed with {error=}")

    def send_message(self, chat_id, message):
        log.info("Sending messages")
        try:
            params = {
                "chat_id": chat_id,
                "text": f"<b><em>{message}</em></b>",
                "parse_mode": "HTML",
            }
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            response = requests.get(url, params=params).json()
            if response['ok']:
                log.info(f"Message sent successfully {response}")
                return True
            else:
                log.error(f"Message send failed {response}")
        except Exception as error:
            log.error(f"Message sending failed for chat id {chat_id}, "
                      f"{error=}")
        return False


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        obj = TelegramBot()

        while True:
            obj.user_updates()

            tweets = UserTweet.objects.filter(
                Q(created_at__gte=timezone.now() - timedelta(minutes=20)) &
                Q(message_sent=False) &
                Q(tweet__accept=True)
            ).order_by('created_at')

            data = {}
            for tg in TelegramAccount.objects.values(
                    'user__id', 'telegram_user_id'
            ):
                data[tg['user__id']] = tg['telegram_user_id']

            for t in tweets:
                if t.user.id in data:
                    twitter_account = t.tweet.twitter_account.name
                    message = f"From: {twitter_account}\n\n{t.tweet.tweet}"
                    status = obj.send_message(
                        data[t.user.id],
                        message,
                    )
                    if status:
                        t.message_sent = True
                        t.save()

            log.info("Sleeping for 15 minutes")
            sleep(900)