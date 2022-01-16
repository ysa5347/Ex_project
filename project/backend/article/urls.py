from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import helloAPI, articlelist, articleview

urlpatterns = [
    path("hello/", helloAPI),
    path("",articlelist),
    path("articleview/<str:pk>/",articleview),
]