from django.contrib import admin

from screener.models import Company, Results


class ResultsAdmin(admin.ModelAdmin):
    list_display = [
        'company', 'date', 'type', 'sales', 'expenses', 'operating_profit',
        'opm', 'other_income', 'interest', 'depreciation', 'profit_before_tax',
        'tax', 'net_profit', 'eps', 'currency', 'unit'
    ]


admin.site.register(Company)
admin.site.register(Results, ResultsAdmin)
