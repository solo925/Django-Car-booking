# Generated by Django 3.2.19 on 2024-05-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbooking', '0003_auto_20240519_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
