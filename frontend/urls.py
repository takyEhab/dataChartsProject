from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("get-data", views.getData, name='getData'),
    path("get-strikes/<str:date>", views.getStrikes, name='getStrikes'),
]
