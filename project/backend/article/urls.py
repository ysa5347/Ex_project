from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import ArticleDelete, ArticleUpdate, helloAPI, ArticleList, getPtcpUser, ArticleView, ArticleCreate#, ArticleCreateView

urlpatterns = [
    path("hello/", helloAPI),
    path("",ArticleList),
    path("<int:pk>/",ArticleView),
    # path("create/", ArticleCreateView),
    path("participant/<int:pk>", getPtcpUser),
    path("create/", ArticleCreate),
    path("delete/<int:pk>/", ArticleDelete),
    path("update/<int:pk>/", ArticleUpdate),
]