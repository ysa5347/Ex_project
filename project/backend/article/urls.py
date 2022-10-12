from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import ArticleDelete, ArticlePtcp, ArticleUpdate, helloAPI, ArticleList, ArticleView, ArticleCreate#, ArticleCreateView

urlpatterns = [
    path("hello/", helloAPI),
    path("",ArticleList),
    path("<int:pk>/",ArticleView, name='view'),
    # path("create/", ArticleCreateView),
    path("create/", ArticleCreate),
    path("delete/<int:pk>/", ArticleDelete),
    path("update/<int:pk>/", ArticleUpdate),
    path("<int:pk>/ptcp/", ArticlePtcp)
]