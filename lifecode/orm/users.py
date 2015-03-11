'''
Created on Jan 23, 2015

@author: nunenuh
'''
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=255)
    displayName = models.CharField(max_length=50)
    active = models.IntegerField()
    role = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

    def __unicode__(self):
        return self.username

class UserProfile(models.Model):
    user = models.ForeignKey(User)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    aboutme = models.TextField()
    birthdate = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=128)
    phone = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile'

    def __unicode__(self):
        return self.first_name
