# Generated by Django 3.2 on 2021-04-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_timeserie_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeserie',
            name='timestamp',
            field=models.DateField(),
        ),
        migrations.AlterUniqueTogether(
            name='timeserie',
            unique_together={('timestamp', 'company')},
        ),
    ]
