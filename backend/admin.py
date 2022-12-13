from django.contrib import admin
from backend.models import Company, UserCompany, TwitterAccount, \
    CompanyTwitterAccount, Tweets, TelegramAccount, UserTweet, \
    FilterKeywords, Messages


class TweetAdmin(admin.ModelAdmin):
    list_display = ['twitter_account', 'tweet', 'accept', 'filter_reason',
                    'tweet_created_at', 'created_at']


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'text', 'update_id']


class UserTweetAdmin(admin.ModelAdmin):
    list_display = ['user', 'message_sent', 'score', 'created_at', 'tweet']


class FilterKeywordsAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'accept', 'score']


class CompanyTweeterAccountInline(admin.TabularInline):
    model = CompanyTwitterAccount


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        CompanyTweeterAccountInline,
    ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(UserCompany)
admin.site.register(TwitterAccount)
admin.site.register(Tweets, TweetAdmin)
admin.site.register(TelegramAccount)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(UserTweet, UserTweetAdmin)
admin.site.register(FilterKeywords, FilterKeywordsAdmin)
