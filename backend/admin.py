from django.contrib import admin
from backend.models import Company, UserCompany, TwitterAccount, \
    CompanyTwitterAccount, Tweets, TelegramAccount, UserTweet


class UserTweetAdmin(admin.ModelAdmin):
    list_display = ['user', 'message_sent', 'score', 'created_at', 'tweet']


admin.site.register(Company)
admin.site.register(UserCompany)
admin.site.register(TwitterAccount)
admin.site.register(CompanyTwitterAccount)
admin.site.register(Tweets)
admin.site.register(TelegramAccount)
admin.site.register(UserTweet, UserTweetAdmin)
