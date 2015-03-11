'''
Created on Jan 23, 2015

@author: nunenuh
'''
from django.db import models
from orm.users import User

class BlogCategory(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name="children")

    name = models.CharField(max_length=255)
    descriptions = models.TextField(default=None, null=True, blank=True)
    counter = models.IntegerField(default=None, null=True, blank=True)
    left = models.IntegerField(default=None, null=True, blank=True)
    right = models.IntegerField(default=None, null=True, blank=True)
    level = models.IntegerField(default=None, null=True, blank=True)
    root = models.IntegerField(default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'blog_category'

    def __unicode__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField(default=None, null=True, blank=True)
    counter = models.IntegerField(default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'blog_tag'

    def __unicode__(self):
        return self.name

class BlogPost(models.Model):
    user = models.ForeignKey(User, related_name="user")
    category = models.ManyToManyField(
        BlogCategory,
        through="BlogPostCategory",
        through_fields=('post', 'category'),
        related_name="post"
    )
    tag = models.ManyToManyField(
        BlogTag,
        through="BlogPostTag",
        through_fields=('post', 'tag'),
        related_name="post"
    )

    title = models.TextField()
    slug = models.CharField(max_length=128)
    content = models.TextField()
    status = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'blog_post'

    def __unicode__(self):
        return self.title


class BlogPostCategory(models.Model):
    post = models.ForeignKey(BlogPost, db_column="post_id")
    category = models.ForeignKey(BlogCategory, db_column="category_id")

    class Meta:
        db_table = 'blog_post_category'

class BlogPostTag(models.Model):
    post = models.ForeignKey(BlogPost, db_column="post_id")
    tag = models.ForeignKey(BlogTag, db_column="tag_id")

    class Meta:
        db_table = 'blog_post_tag'

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comment")
    parent = models.ForeignKey('self', default=None, null=True, blank=True)

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255,default=None)
    site = models.CharField(max_length=255,default=None)
    content = models.TextField()
    approved = models.IntegerField()
    ip_address = models.CharField(max_length=45, default=None)
    user_agent = models.CharField(max_length=45, default=None)
    platform = models.CharField(max_length=45, default=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'blog_comment'

    def __unicode__(self):
        return self.name
