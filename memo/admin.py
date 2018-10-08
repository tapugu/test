from django.contrib import admin

from memo.models import Method, Module, Argument

# Register your models here.
admin.site.register(Method)
admin.site.register(Module)
admin.site.register(Argument)
