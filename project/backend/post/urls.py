from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import helloAPI, postlist

urlpatterns = [
    path("hello/", helloAPI),
    path("postlist/",postlist),
]