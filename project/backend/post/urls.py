from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import PostDelete, PostUpdate, helloAPI, PostList, PostView, PostCreate#, PostCreateView

urlpatterns = [
    path("hello/", helloAPI),
    path("",PostList),
    path("view/<int:pk>/",PostView),
    # path("create/", PostCreateView),
    path("create/<int:pk>/", PostCreate),
    path("delete/<int:pk>/", PostDelete),
    path("update/<int:pk>/", PostUpdate),
]