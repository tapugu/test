# Generated by Django 2.0.6 on 2018-09-17 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0002_method_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='argument',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='memo.Method', verbose_name='メソッド'),
        ),
    ]
