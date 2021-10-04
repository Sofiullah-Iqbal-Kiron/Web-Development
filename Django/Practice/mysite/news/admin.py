from django.contrib import admin
from django.urls.resolvers import RegexPattern
from .models import Article, Reporter

# Register your models here.

admin.site.register(Reporter)
admin.site.register(Article)