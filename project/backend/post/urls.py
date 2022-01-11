from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import helloAPI, post_page

urlpatterns = [
    path("hello/", helloAPI),
    path("", post_page)
]