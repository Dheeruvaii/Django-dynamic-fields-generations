from django.contrib import admin
from django.urls import path,include
from .views import*
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router= routers.DefaultRouter()
router.register('Author', AuthViewSet,basename='author-list')

urlpatterns = [
    path('',include(router.urls)),
    
]
