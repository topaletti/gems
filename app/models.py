from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    stock_exchange = models.CharField(max_length=50, blank=True)
    ticker = models.CharField(max_length=12, blank=True)
    price = models.FloatField(default=0, blank=True)
    price_history = models.JSONField(default=[1] * 365, blank=True)
    currency = models.CharField(max_length=3, blank=True)
    website = models.CharField(max_length=50, blank=True)
    xing_profile = models.CharField(max_length=50, blank=True)
    kununu_profile = models.CharField(max_length=50, blank=True)
    kununu_score = models.FloatField(default=0, blank=True)
    industry = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def price_history_points(self):
        price_history = self.price_history
        min_price = min(price_history)
        max_price = max(price_history)
        price_spread = max_price - min_price
        if price_spread == 0:
            price_spread = 0.01
        pixel_per_unit = 260 / price_spread
        points = []
        for price in price_history:
            points.append(round((280 - (price - min_price) * pixel_per_unit),2))
        return points

    class Meta:
        verbose_name_plural = 'companies'


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    companies = models.ManyToManyField(Company, through='PortfolioCompany')


class PortfolioCompany(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    buy_price = models.FloatField(default=0)
    bought_before = models.BooleanField(default=False)
    currently_holding = models.BooleanField(default=True)
    last_buy_date = models.DateTimeField(blank=True)
    last_sell_date = models.DateTimeField(blank=True)

    class Meta:
        db_table = 'app_portfolio_company'
        verbose_name = 'portfolio-company association'
        verbose_name_plural = 'portfolio-company associations'
