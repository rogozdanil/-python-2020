# Generated by Django 3.1.4 on 2021-01-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0004_auto_20210114_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='commands',
            name='stadium',
            field=models.CharField(default='чикаго', max_length=100, verbose_name='Стадион'),
        ),
        migrations.AddField(
            model_name='commands',
            name='winers',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Чемпионство'),
        ),
    ]
