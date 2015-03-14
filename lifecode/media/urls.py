'''
Created on Jan 26, 2015

@author: nunenuh
'''
from django.conf.urls import url, include
from rest_framework import routers
from media import views

router = routers.SimpleRouter(trailing_slash=False)
# router.register(r'upload', views.FileUploadView.as_view())
router.register(r'file', views.MediaFileViewSet)
router.register(r'album', views.MediaAlbumViewSet)
router.register(r'albumfile', views.MediaAlbumFileViewSet)


urlpatterns = [
    url(r'^media/upload', views.FileUploadView.as_view()),
    url(r'^media/file/filter', views.MediaFileFilterList.as_view()),
    url(r'^media/', include(router.urls))
]
