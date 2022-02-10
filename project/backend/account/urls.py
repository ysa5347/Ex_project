from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from .views import IsIdValid

urlpatterns = [
    path("create/", views.createUser),
    path("isidvalid/", IsIdValid),
    
]