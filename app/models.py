from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    revenue_drive = models.CharField(max_length=500, blank=True)
    future_endeavours = models.CharField(max_length=500, blank=True)
    stock_exchange = models.CharField(max_length=50, blank=True)
    ticker = models.CharField(max_length=12, blank=True)
    price = models.FloatField(default=0, blank=True)
    price_history = models.JSONField(default={"placeholder": 0}, blank=True)
    currency = models.CharField(max_length=3, blank=True)
    website = models.CharField(max_length=50, blank=True)
    xing_profile = models.CharField(max_length=50, blank=True)
    kununu_profile = models.CharField(max_length=50, blank=True)
    kununu_score = models.FloatField(default=0, blank=True)
    industry = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def revenue_drive_list(self):
        return self.revenue_drive.split('; ')

    def future_endeavours_list(self):
        return self.future_endeavours.split('; ')

    def price_history_points(self):
        price_history = self.price_history
        prices = []
        for price in price_history:
            prices.append(price_history[price])
        prices = prices[0::5] # getting every fifth
        min_price = min(prices)
        max_price = max(prices)
        price_spread = max_price - min_price
        if price_spread == 0:
            price_spread = 0.01
        graph_height = 140 # tightly coupled with template
        pixel_per_unit = graph_height / price_spread
        points = []
        for price in prices:
            points.append(round(((graph_height + 20) - (price - min_price) * pixel_per_unit),2))
        if len(points) < 252: # add padding
            padding_length = 252 - len(points)
            padding = [0]*padding_length
            points = [*padding, *points]
        return points

    def five_year_performance(self):
        price_history = list(self.price_history.values())
        total_history_length = len(price_history)
        last_index = total_history_length - 1
        if total_history_length < 1260:
            displayed_history_length = total_history_length
        else:
            displayed_history_length = 1260
        first_index = total_history_length - displayed_history_length
        if price_history[0] == 0: # placeholder dict
            return 0
        else:
            return int(price_history[last_index] / price_history[first_index] * 100 - 100)

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
