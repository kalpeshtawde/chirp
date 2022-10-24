from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TelegramAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telegram_user_id = models.BigIntegerField(unique=True)
    is_bot = models.BooleanField()
    chat_id = models.BigIntegerField(unique=True)

    class Meta:
        verbose_name = 'Telegram Account'

    def __str__(self):
        return str(self.user)


class Company(models.Model):
    name = models.CharField(max_length=256, unique=True)

    class Meta:
        verbose_name = 'Companies'

    def __str__(self):
        return str(self.name)


class UserCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'My Tracking List'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} :" \
               f" {str(self.company)}"


class TwitterAccount(models.Model):
    acct_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Twitter Accounts'

    def __str__(self):
        return f"{self.name} [@{self.username}]"


class CompanyTwitterAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    twitter_account = models.ForeignKey(
        TwitterAccount, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Company Twitter Accounts'

    def __str__(self):
        return str(f"{self.company} : {self.twitter_account}")


class Tweets(models.Model):
    twitter_account = models.ForeignKey(TwitterAccount,
                                        on_delete=models.CASCADE)
    tweet_id = models.BigIntegerField(unique=True)
    tweet = models.CharField(max_length=512)
    tweet_created_at = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Tweets'

    def __str__(self):
        return str(
            f"{self.twitter_account} : {self.tweet} : {self.tweet_created_at}"
        )


class UserTweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    message_sent = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'UserTweet'

    def __str__(self):
        return str(
            f"{self.user.first_name} : {self.tweet.tweet}"
        )
