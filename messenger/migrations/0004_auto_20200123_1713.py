# Generated by Django 3.0.2 on 2020-01-23 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_auto_20200120_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['date_added']},
        ),
    ]
