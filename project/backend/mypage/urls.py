from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import getUser

urlpatterns = [
    path("getuser/", getUser),
]