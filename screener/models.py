from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256)
    exch_name = models.CharField(max_length=50)
    exch_code = models.CharField(max_length=50)
    website = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Companies"

    def __str__(self):
        return str(self.name)


class Results(models.Model):
    TYPE = [
        ('Q', 'Quarterly'),
        ('A', 'Annually'),
    ]
    CURRENCY = [
        ('INR', 'Indian Rupees'),
        ('USD', 'American Dollar'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE, default='Q')
    sales = models.IntegerField(blank=True, null=True)
    expenses = models.IntegerField(blank=True, null=True)
    operating_profit = models.IntegerField(blank=True, null=True)
    opm = models.IntegerField(blank=True, null=True)
    other_income = models.IntegerField(blank=True, null=True)
    interest = models.IntegerField(blank=True, null=True)
    depreciation = models.IntegerField(blank=True, null=True)
    profit_before_tax = models.IntegerField(blank=True, null=True)
    tax = models.IntegerField(blank=True, null=True)
    net_profit = models.IntegerField(blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=20, choices=CURRENCY, default='INR')
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Result"
        ordering = ('date',)

    def __str__(self):
        return str(f"{self.company} {self.date}")


class BalanceSheet(models.Model):
    TYPE = [
        ('Q', 'Quarterly'),
        ('A', 'Annually'),
    ]
    CURRENCY = [
        ('INR', 'Indian Rupees'),
        ('USD', 'American Dollar'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE, default='A')
    share_capital = models.IntegerField(blank=True, null=True)
    reserves = models.IntegerField(blank=True, null=True)
    borrowings = models.IntegerField(blank=True, null=True)
    other_liabilities = models.IntegerField(blank=True, null=True)
    total_liabilities = models.IntegerField(blank=True, null=True)
    fixed_assets = models.IntegerField(blank=True, null=True)
    cwip = models.IntegerField(blank=True, null=True)
    investments = models.IntegerField(blank=True, null=True)
    other_assets = models.IntegerField(blank=True, null=True)
    total_assets = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=20, choices=CURRENCY, default='INR')
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Balance Sheet"
        ordering = ('date',)

    def __str__(self):
        return str(f"{self.company} {self.date}")


class CashFlow(models.Model):
    TYPE = [
        ('Q', 'Quarterly'),
        ('A', 'Annually'),
    ]
    CURRENCY = [
        ('INR', 'Indian Rupees'),
        ('USD', 'American Dollar'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE, default='A')
    operating = models.IntegerField(blank=True, null=True)
    investing = models.IntegerField(blank=True, null=True)
    financing = models.IntegerField(blank=True, null=True)
    net = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=20, choices=CURRENCY, default='INR')
    unit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Cash Flow"
        ordering = ('date',)

    def __str__(self):
        return str(f"{self.company} {self.date}")


class Ratios(models.Model):
    TYPE = [
        ('Q', 'Quarterly'),
        ('A', 'Annually'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE, default='A')
    debtor_days = models.IntegerField(blank=True, null=True)
    inventory_days = models.IntegerField(blank=True, null=True)
    days_payable = models.IntegerField(blank=True, null=True)
    cash_conversion_cycle = models.IntegerField(blank=True, null=True)
    working_capital_days = models.IntegerField(blank=True, null=True)
    roce_pct = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Ratios"
        ordering = ('date',)

    def __str__(self):
        return str(f"{self.company} {self.date}")


class Shareholding(models.Model):
    TYPE = [
        ('Q', 'Quarterly'),
        ('A', 'Annually'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE, default='Q')
    promoters_pct = models.FloatField(blank=True, null=True)
    fii_pct = models.FloatField(blank=True, null=True)
    dii_pct = models.FloatField(blank=True, null=True)
    government_pct = models.FloatField(blank=True, null=True)
    public_pct = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = "Shareholding"
        ordering = ('date',)

    def __str__(self):
        return str(f"{self.company} {self.date}")
