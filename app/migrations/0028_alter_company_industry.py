# Generated by Django 3.2 on 2021-04-17 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_company_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(max_length=60),
        ),
    ]
