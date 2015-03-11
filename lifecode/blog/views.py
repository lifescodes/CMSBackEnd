from django.shortcuts import render
from orm.blog import *
from rest_framework import viewsets
from blog.serializers import *

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogCommentViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

class BlogCategoryTreeViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.exclude(parent__isnull=False)
    serializer_class = BlogCategoryTreeSerializer

class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all().order_by('parent')
    serializer_class = BlogCategorySerializer

class BlogTagViewSet(viewsets.ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer

class BlogPostCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogPostCategory.objects.all()
    serializer_class = BlogPostCategorySerializer

class BlogPostTagViewSet(viewsets.ModelViewSet):
    queryset = BlogPostTag.objects.all()
    serializer_class = BlogPostTagSerializer
