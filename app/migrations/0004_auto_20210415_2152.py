# Generated by Django 3.2 on 2021-04-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210415_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='beta',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='fifty_two_week_change',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='fifty_two_week_high',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='fifty_two_week_low',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='market_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='payout_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='pb_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='peg_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='previous_close',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='company',
            name='trailing_pe_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
