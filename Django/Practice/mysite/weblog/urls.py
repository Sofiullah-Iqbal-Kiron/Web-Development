from django.urls import path
from . import views

app_name = "weblog"
urlpatterns = [
    path('', views.index, name='index')
]
