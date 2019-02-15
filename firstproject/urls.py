from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),
    path('hi/', wordcount.views.hi, name="hi"),
    path('hi2/', wordcount.views.hi2, name="hi2"),
    path('hi3/', wordcount.views.hi3, name="hi3"),
    path('hi4/', wordcount.views.hi4, name="hi4"),
    path('hi6/', wordcount.views.hi6, name="hi6"),
]
