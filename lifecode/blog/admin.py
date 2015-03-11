from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib import admin
from orm.blog import *

admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(BlogCategory)
admin.site.register(BlogTag)
admin.site.register(BlogPostCategory)
admin.site.register(BlogPostTag)
