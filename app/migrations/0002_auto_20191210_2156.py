# Generated by Django 2.1.2 on 2019-12-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sample_9',
            field=models.IntegerField(blank=True, choices=[(1, '人参'), (2, '大根'), (3, 'じゃがいも'), (4, 'キャベツ'), (5, 'ホウレンソウ'), (6, 'ピーマン'), (7, 'なんでもいい')], null=True, verbose_name='ほしい野菜'),
        ),
    ]
