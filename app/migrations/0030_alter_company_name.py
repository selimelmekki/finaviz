# Generated by Django 3.2 on 2021-04-17 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20210417_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
