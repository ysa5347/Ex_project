from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from .views import IsIdValid, loginUser, logoutUser, viewsession

urlpatterns = [
    path("signup/", views.createUser),
    path("isidvalid/", IsIdValid),
    path("login/", loginUser),
    path("logout/", logoutUser),
    path("view/", viewsession),
]