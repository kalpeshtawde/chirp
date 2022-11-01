import re
import logging
import time

from django.core.management.base import BaseCommand

from backend.models import Tweets, FilterKeywords

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class TweetRefiner:
    
    def __init__(self):
        pass

    @staticmethod
    def small_tweet(tweet):
        return False if len(tweet.split(" ")) < 10 else True

    def run(self):
        accept = {}
        score = {}
        for k in FilterKeywords.objects.all():
            accept[k.keyword] = k.accept
            score[k.keyword] = k.score

        for t in Tweets.objects.filter(accept__isnull=True):
            """
            If tweet is too small and hence not informative, reject it.
            """
            tweet = t.tweet.lower()

            t.accept = self.small_tweet(tweet)
            if not t.accept:
                t.filter_reason = "Tweet too small"

            """
            If unaccepted keyword present in tweet, mark it for rejection.
            """
            if t.accept:
                for k in accept:
                    if accept[k] is False and re.search(k.lower(), tweet):
                        t.accept = False
                        t.filter_reason = f"Tweet has unaccepted keyword [{k}]"
                        break

            """
            If tweet marked for rejection but has a keyword with 100 score,
            accept the tweet.
            """
            if not t.accept:
                for k in score:
                    if int(score[k]) == 100 and re.search(k.lower(), tweet):
                        t.accept = True
                        break

            if t.accept:
                log.info(f"Tweet [{tweet}] accepted to be sent")
            else:
                log.info(f"Tweet [{tweet}] rejected")
                
            t.save()


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **option):
        while True:
            obj = TweetRefiner()
            obj.run()
            log.info("Sleeping for 5 minutes")
            time.sleep(300)
