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
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework import routers


class HomeTemplateView(ArticleViewSet):
    template_name = 'index.html'

# router = routers.DefaultRouter()
# router.register(r'articles', views.ArticleViewSet, 'Article')


schema_view = get_schema_view(
    openapi.Info(
        title="Ex-finder",
        default_version='v1',
        description="Ex-finder backend API docs",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    # 이 아랫 부분은 우리가 사용하는 app들의 URL들을 넣습니다.
    path('admin/', admin.site.urls),
    path('', helloAPI),
    path('article/', include('article.urls')),
    path('account/', include('account.urls')),
    path('mypage/', include('mypage.urls'))
    # path('', HomeTemplateView.as_view(), name='home')
]
