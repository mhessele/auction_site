# Generated by Django 3.0.6 on 2020-06-01 17:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0003_auto_20200601_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='min_price_step',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lot',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 4, 17, 15, 54, tzinfo=utc)),
        ),
    ]
