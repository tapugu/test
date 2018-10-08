from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, DetailView, ListView
from .models import Module, Method, Argument
import datetime, time



class IndexView(TemplateView):
    template_name = "index.html"


class MemoView(ListView):
    template_name = "memo.html"
    model = Module



class DetailView(DetailView):
    template_name = "detail.html"
    model = Module



    # 変数に値を入れてTemplatesで使用できる
    # get_context_dataをオーバーライドして使用する
    def get_context_data(self, **kwargs):
        obj_pk = Module.objects.get(pk=self.kwargs["pk"])
        argument_list = {}
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["methods"] = Method.objects.filter(module__name=obj_pk)
        context["arguments"] = Argument.objects.all()
        context["foo"] = "ber"
        context["time"] = time.time()
        for method in context["methods"]:
            argument_list[method.name] = Argument.objects.filter(method__name=method)
        context["argument_list"] = argument_list
        return context



index = IndexView.as_view()
memo = MemoView.as_view()
detail = DetailView.as_view()
