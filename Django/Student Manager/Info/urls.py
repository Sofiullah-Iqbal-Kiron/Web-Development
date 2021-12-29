from django.urls import path

from . import views

# List of paths named exactly 'urlpatterns'.
urlpatterns = [
    path('', views.index, name="index")
]
