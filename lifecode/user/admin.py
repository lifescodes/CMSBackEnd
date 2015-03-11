from django.contrib import admin

# Register your models here.
from orm.users import User, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
