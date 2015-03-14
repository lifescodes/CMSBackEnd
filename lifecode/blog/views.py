from django.shortcuts import render
from orm.blog import *
from rest_framework import viewsets
from blog.serializers import *

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import views
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
import django_filters


class BlogPostFilter(django_filters.FilterSet):
    # manufacturer = django_filters.CharFilter(name="file_type__name")
    class Meta:
        model = BlogPost
        fields = ['title','status']

class BlogPostFilterListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_class = BlogPostFilter

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListSerializer

class BlogCommentViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

class BlogCategoryTreeViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.exclude(parent__isnull=False)
    serializer_class = BlogCategoryTreeSerializer

class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all().order_by('parent')
    serializer_class = BlogCategorySerializer



class BlogPostCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = BlogPostCategory
        fields = ['category','post']

class BlogPostCategoryFilterListView(generics.ListAPIView):
    queryset = BlogPostCategory.objects.all()
    serializer_class = BlogPostCategorySerializer
    filter_class = BlogPostCategoryFilter

class BlogPostCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogPostCategory.objects.all()
    serializer_class = BlogPostCategorySerializer



class BlogTagFilter(django_filters.FilterSet):
    # manufacturer = django_filters.CharFilter(name="file_type__name")
    class Meta:
        model = BlogTag
        fields = ['name','counter']

class BlogTagFilterListView(generics.ListAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
    filter_class = BlogTagFilter

class BlogTagViewSet(viewsets.ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer



class BlogPostTagFilter(django_filters.FilterSet):
    class Meta:
        model = BlogPostTag
        fields = ['tag','post']

class BlogPostTagFilterListView(generics.ListAPIView):
    queryset = BlogPostTag.objects.all()
    serializer_class = BlogPostTagSerializer
    filter_class = BlogPostTagFilter

class BlogPostTagViewSet(viewsets.ModelViewSet):
    queryset = BlogPostTag.objects.all()
    serializer_class = BlogPostTagSerializer
