'''
Created on Jan 23, 2015

@author: nunenuh
'''

from django.db import models
from orm.users import User


class Role(models.Model):

    class Meta:
        db_table = 'role'

    user = models.ManyToManyField(User)
    name  = models.CharField(max_length=48)
    parent = models.ForeignKey('self')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name


class Permission(models.Model):

    class Meta:
        db_table = 'permission'

    role = models.ManyToManyField(Role)
    name  = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
