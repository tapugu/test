# Generated by Django 2.0.6 on 2018-09-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0007_auto_20180930_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='argument',
            name='order',
            field=models.IntegerField(null=True, verbose_name='表示順'),
        ),
        migrations.AddField(
            model_name='method',
            name='order',
            field=models.IntegerField(null=True, verbose_name='表示順'),
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=models.IntegerField(null=True, verbose_name='表示順'),
        ),
    ]