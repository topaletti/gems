# Generated by Django 3.2.5 on 2021-09-25 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210925_0739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='portfoliocompany',
            options={'verbose_name': 'portfolio-company association', 'verbose_name_plural': 'portfolio-company associations'},
        ),
        migrations.AlterModelTable(
            name='portfoliocompany',
            table='portfolio_company',
        ),
    ]
