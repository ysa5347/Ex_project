from django.urls import path
from .views import getUser, getUserArticle, getUserPtcp

urlpatterns =[
    path("getuser/", getUser),
    path("getarticle/", getUserArticle),
    path("getuserptcp/", getUserPtcp),
]
    
