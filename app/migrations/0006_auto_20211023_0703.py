# Generated by Django 3.2.5 on 2021-10-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210925_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='future_endeavours',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='company',
            name='revenue_drive',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='price_history',
            field=models.JSONField(blank=True, default={'placeholder': 0}),
        ),
    ]
