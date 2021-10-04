from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('reporters/', views.reporters, name='reporters')]
