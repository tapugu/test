from django.db import models
import datetime

# Create your models here.


class Module(models.Model):

    class Meta:
        db_table = "module"

    name = models.CharField(verbose_name="モジュール", max_length=255)
    comment = models.CharField(verbose_name="モジュールの説明", max_length=1000)
    order = models.IntegerField(verbose_name="表示順", null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        

class Method(models.Model):
    """メソッドモデル"""
    class Meta:
        db_table = "method"

    module = models.ForeignKey(Module, verbose_name="モジュール", on_delete=models.PROTECT)
    name = models.CharField(verbose_name="メソッド", max_length=255)
    header = models.CharField(verbose_name="見出し", max_length=255, null=True)
    comment = models.CharField(verbose_name="説明", max_length=255)
    syntax = models.CharField(verbose_name="構文", max_length=255)
    order = models.IntegerField(verbose_name="表示順", null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Argument(models.Model):
    """引数モデル"""
    class Meta:
        db_table = "argument"

    method = models.ForeignKey(Method, verbose_name="メソッド", on_delete=models.PROTECT)
    name = models.CharField(verbose_name="引数", max_length=255)
    type = models.CharField(verbose_name="引数の型", max_length=255)
    comment = models.CharField(verbose_name="引数の説明", max_length=255)
    order = models.IntegerField(verbose_name="表示順", null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



