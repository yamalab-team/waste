# Generated by Django 3.0.6 on 2020-07-01 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200702_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f_item',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 9, 1, 38, 57, 116487), null=True, verbose_name='購入期限'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='delete',
            field=models.BooleanField(default=False, verbose_name='削除済み'),
        ),
    ]
