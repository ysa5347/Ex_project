from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from .views import IsIdValid

urlpatterns = [
    path("signup/", views.createUser),
    path("isidvalid/", IsIdValid),
    
]