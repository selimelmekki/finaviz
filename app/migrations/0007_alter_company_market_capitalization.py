# Generated by Django 3.2 on 2021-04-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210415_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='market_capitalization',
            field=models.BigIntegerField(),
        ),
    ]
