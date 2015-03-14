'''
Created on Jan 26, 2015

@author: nunenuh
'''
from django.conf.urls import url, include
from rest_framework import routers
from blog import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'post', views.BlogPostViewSet)
router.register(r'category', views.BlogCategoryViewSet)
router.register(r'category-tree', views.BlogCategoryTreeViewSet)
router.register(r'postcategory', views.BlogPostCategoryViewSet)
router.register(r'tag', views.BlogTagViewSet)
router.register(r'posttag', views.BlogPostTagViewSet)
router.register(r'comment', views.BlogCommentViewSet)

urlpatterns = [
    url(r'^blog/post/list', views.BlogPostListView.as_view()),
    url(r'^blog/post/filter', views.BlogPostFilterListView.as_view()),
    url(r'^blog/tag/filter', views.BlogTagFilterListView.as_view()),
    url(r'^blog/posttag/filter', views.BlogPostTagFilterListView.as_view()),
    url(r'^blog/postcategory/filter', views.BlogPostCategoryFilterListView.as_view()),
    url(r'^blog/', include(router.urls))
]
