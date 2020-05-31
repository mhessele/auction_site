# Generated by Django 3.0.6 on 2020-05-31 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200531_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]