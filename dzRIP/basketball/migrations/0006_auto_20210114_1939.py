# Generated by Django 3.1.4 on 2021-01-14 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0005_auto_20210114_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commands',
            old_name='commands',
            new_name='players',
        ),
    ]
