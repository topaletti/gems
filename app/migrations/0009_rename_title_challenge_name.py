# Generated by Django 3.2.5 on 2022-04-01 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220401_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='title',
            new_name='name',
        ),
    ]
