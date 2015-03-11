'''
Created on Jan 26, 2015

@author: nunenuh
'''
from django.conf.urls import url, include
from rest_framework import routers
from user import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'user', views.UserViewSet)
router.register(r'profile', views.UserProfileViewSet)

urlpatterns = [
    url(r'^user/', include(router.urls))
]
