from django.contrib import admin

from screener.models import *


class ResultsAdmin(admin.ModelAdmin):
    list_display = [
        'company', 'date', 'type', 'sales', 'expenses', 'operating_profit',
        'opm', 'other_income', 'interest', 'depreciation', 'profit_before_tax',
        'tax', 'net_profit', 'eps', 'currency', 'unit'
    ]


class BalanceSheetAdmin(admin.ModelAdmin):
    list_display = [
        'company', 'date', 'type', 'share_capital', 'reserves',
        'borrowings', 'other_liabilities', 'total_liabilities', 'fixed_assets',
        'cwip', 'investments', 'other_assets', 'total_assets', 'currency',
        'unit'
    ]


class CashFlowAdmin(admin.ModelAdmin):
    list_display = [
        'company', 'date', 'type', 'operating', 'investing', 'financing',
        'net', 'currency', 'unit'
    ]


class RatiosAdmin(admin.ModelAdmin):
    list_display = [
        'company', 'date', 'type', 'debtor_days', 'inventory_days',
        'days_payable', 'cash_conversion_cycle', 'working_capital_days',
        'roce_pct'
    ]


class ShareholdingAdmin(admin.ModelAdmin):
    list_display = [
        'company', 'date', 'type', 'promoters_pct', 'fii_pct', 'dii_pct',
        'government_pct', 'public_pct'
    ]


admin.site.register(Company)
admin.site.register(Results, ResultsAdmin)
admin.site.register(BalanceSheet, BalanceSheetAdmin)
admin.site.register(CashFlow, CashFlowAdmin)
admin.site.register(Ratios, RatiosAdmin)
admin.site.register(Shareholding, ShareholdingAdmin)
