# Generated by Django 2.0.6 on 2018-09-23 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0003_auto_20180917_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='argument',
            old_name='argument_comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='argument',
            old_name='argument_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='module_comment',
            new_name='comment',
        ),
    ]
