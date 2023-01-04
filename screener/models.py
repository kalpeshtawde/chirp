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

    def __str__(self):
        return str(f"{self.company} {self.date}")

