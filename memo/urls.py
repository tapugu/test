from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo, name='memo'),
    path("<int:pk>/", views.detail, name="memo")
]