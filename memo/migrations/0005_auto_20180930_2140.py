# Generated by Django 2.0.6 on 2018-09-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0004_auto_20180923_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='comment',
            field=models.CharField(max_length=1000, verbose_name='モジュールの説明'),
        ),
    ]