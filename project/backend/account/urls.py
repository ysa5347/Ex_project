from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from .views import IsIdValid, loginUser, logoutUser, viewsession

urlpatterns = [
    path("signup/", views.createUser, name='signup'),
    path("isidvalid/", IsIdValid, name='isIdValid'),
    path("login/", loginUser, name='login'),
    path("logout/", logoutUser, name='logout'),
    path("view/", viewsession, name='view'),
]