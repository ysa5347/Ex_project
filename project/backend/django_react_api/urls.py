"""django_react_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from article.views import ArticleViewSet, helloAPI
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers


class HomeTemplateView(ArticleViewSet):
    template_name = 'index.html'

# router = routers.DefaultRouter()
# router.register(r'articles', views.ArticleViewSet, 'Article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', helloAPI),
    path('article/', include('article.urls')),
    path('account/', include('account.urls')),
    path('mypage/', include('mypage.urls'))
    # path('', HomeTemplateView.as_view(), name='home')
]
