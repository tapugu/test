# Generated by Django 2.0.6 on 2018-09-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0005_auto_20180930_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='header',
            field=models.CharField(max_length=255, null=True, verbose_name='見出し'),
        ),
    ]
