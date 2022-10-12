from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import ArticleDelete, ArticlePtcp, ArticleUpdate, helloAPI, ArticleList, ArticleView, ArticleCreate#, ArticleCreateView

urlpatterns = [
    path("hello/", helloAPI),
    path("",ArticleList, name='list'),
    path("<int:pk>/",ArticleView, name='view'),
    # path("create/", ArticleCreateView),
    path("create/", ArticleCreate, name='create'),
    path("delete/<int:pk>/", ArticleDelete, name='delete'),
    path("update/<int:pk>/", ArticleUpdate, name='update'),
    path("<int:pk>/ptcp/", ArticlePtcp, name='ptcp')
]