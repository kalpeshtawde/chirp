import os
import requests
import logging
from datetime import datetime, timedelta
from time import sleep

from django.core.management.base import BaseCommand

from backend.models import UserCompany, CompanyTwitterAccount, Tweets, UserTweet

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Tweet:
    def __init__(self):
        self.bearer_token = os.environ.get("BEARER_TOKEN")


class UserTweets(Tweet):
    def __init__(self, start_date=None, end_date=None, user_id=None,
                 next_token=None):
        super().__init__()
        self.start_date = start_date
        self.end_date = end_date
        self.next_token = next_token
        self.user_id = user_id

    def create_url(self):
        return f"https://api.twitter.com/2/users/{self.user_id}/tweets"

    def get_params(self):
        return {
            "tweet.fields": "author_id,created_at",
            "expansions": "author_id",
            "user.fields": "name,username",
            "start_time": self.start_date,
            "end_time": self.end_date,
            "pagination_token": self.next_token,
            "exclude": "replies,retweets",
        }

    def bearer_oauth(self, r):
        r.headers["Authorization"] = f"Bearer {self.bearer_token}"
        r.headers["User-Agent"] = "v2UserTweetsPython"
        return r

    def connect_to_endpoint(self, url, params):
        response = requests.request("GET", url, auth=self.bearer_oauth,
                                    params=params)
        if response.status_code != 200:
            log.error(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def run(self):
        url = self.create_url()
        params = self.get_params()
        json_response = self.connect_to_endpoint(url, params)
        return json_response


class Command(BaseCommand):
    def get_user_tweets(self, user_id, start_date, end_date, next_token=None,
                        prev_tweets=[]):

        log.info(f"Getting user tweets with token {next_token}")

        tweets = prev_tweets
        ut = UserTweets(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
            next_token=next_token
        )

        user_tweets = ut.run()

        tweets.extend([(tweet['id'], tweet['text'], tweet['created_at']) for
                       tweet in user_tweets.get('data', [])])

        if 'next_token' in user_tweets['meta']:
            self.get_user_tweets(user_id, start_date, end_date,
                            user_tweets['meta']['next_token'], tweets)

        return tweets

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        tweet_duration = int(os.getenv("TWEET_DURATION", 20))
        while True:
            companies = [uc['company__id'] for uc in UserCompany.objects.values(
                'company__id').distinct()]

            if companies:
                log.info(f"Found companies {len(companies)}")

                start_date = (datetime.utcnow() - timedelta(
                    minutes=tweet_duration)).strftime('%Y-%m-%dT%H:%M:%SZ')
                end_date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

                for company in CompanyTwitterAccount.objects.filter(
                        company__id__in=companies):
                    twitter_account_id = company.twitter_account.acct_id

                    log.info(f"Getting tweets for User {twitter_account_id}")

                    tweets = self.get_user_tweets(twitter_account_id, start_date, end_date)
                    if tweets:
                        for tweet in tweets:
                            tweet_obj, created = Tweets.objects.get_or_create(
                                tweet_id=tweet[0],
                                defaults={
                                    'twitter_account': company.twitter_account,
                                    'tweet': tweet[1],
                                    'tweet_created_at': tweet[2],
                                }
                            )
                            if created:
                                users = UserCompany.objects.filter(
                                    company=company.company
                                )
                                for u in users:
                                    print(u)
                                    UserTweet(user=u.user,
                                              tweet=tweet_obj).save()
            else:
                log.warning("No companies found to process")

            log.info("Sleeping for 15 minutes")
            sleep(900)
