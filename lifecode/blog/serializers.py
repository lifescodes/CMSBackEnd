'''
Created on Jan 26, 2015

@author: nunenuh
'''
from orm.blog import *
from orm.users import User
from user.serializers import UserSerializer
from rest_framework import serializers

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class BlogCategorySerializer(serializers.ModelSerializer):
    # child = BlogCategoryChildSerializer(many=True, read_only=True);
    # children = RecursiveField(many=True, read_only=True);
    class Meta:
        model = BlogCategory
        fields = (
            'id', 'parent', 'name', 'descriptions', 'counter',
            'left', 'right', 'level', 'root', 'created','modified'
        )

class BlogCategoryTreeSerializer(serializers.ModelSerializer):
    # child = BlogCategoryChildSerializer(many=True, read_only=True);
    children = RecursiveField(many=True, read_only=True);
    class Meta:
        model = BlogCategory
        fields = (
            'id', 'parent', 'name', 'descriptions', 'counter',
            'left', 'right', 'level', 'root', 'created','modified',
            'children'
        )

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = (
            'id', 'name', 'descriptions', 'counter', 'created', 'modified'
        )


class BlogPostListSerializer(serializers.ModelSerializer):
    comment = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="comment-detail")
    # user = UserSerializer(many=False, read_only=True)
    category = BlogCategorySerializer(many=True, read_only=True)
    tag = BlogTagSerializer(many=True, read_only=True)
    class Meta:
        model = BlogPost
        fields = (
            'id','user','title','slug','content','status',
            'category', 'tag', 'created','modified','comment'
        )


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
            'id','user','title','slug','content','status',
            'created','modified'
        )

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = (
            'id', 'post', 'parent', 'name', 'email', 'content', 'approved',
            'created', 'modified'
        )


class BlogPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostCategory
        fields = ('id','post','category')

class BlogPostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostTag
        fields = ('id','post','tag')
