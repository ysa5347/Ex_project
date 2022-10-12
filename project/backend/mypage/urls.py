
from django.urls import path
from .views import getUser, getUserArticle, getUserPtcp

urlpatterns =[
    path("getuser/", getUser, name='getuser'),
    path("getarticle/", getUserArticle, name='getarticle'),
    path("getuserptcp/", getUserPtcp, name='getuserptcp'),
]
