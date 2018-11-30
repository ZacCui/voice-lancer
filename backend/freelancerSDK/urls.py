
from rest_framework import routers
from django.urls import path, include
from freelancerSDK.views import hello, search_project, create_fixed_project

urlpatterns = [
    path('', hello),
    path('search_project', search_project),
    path('create_fixed_project', create_fixed_project),
]