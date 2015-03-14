'''
Created on Feb 17, 2015

@author: nunenuh
'''

from django.db import models
from orm.users import User

class File(models.Model):
    user = models.ForeignKey(User)

    name = models.TextField()
    descriptions = models.TextField()
    file_name = models.TextField()
    file_size = models.TextField()
    file_type = models.charField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'file'

    def __unicode__(self):
        return self.name

class FileCategory(models.Model):
    file = models.ManyToManyField(File)

    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    counter = models.IntegerField()
    left = models.IntegerField()
    right = models.IntegerField()
    level = models.IntegerField()
    root = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'file_category'

    def __unicode__(self):
        return self.name
