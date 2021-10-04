from django.urls import path
from . import views

app_name = "isaac_college"
urlpatterns = [
    path('', views.index, name='index'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('tutorials/html_form/', views.html_form, name='html_form')
]
