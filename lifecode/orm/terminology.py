'''
Created on Jan 23, 2015

@author: nunenuh
'''


from django.db import models
from orm.blog import *


class Term(models.Model):
    
    class Meta:
        db_table = 'term'
        
    name = models.TextField()
    slug = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
   
    def __unicode__(self):
        return self.name

class Taxonomy(models.Model):
    class Meta:
        db_table = 'taxonomy'
    
    term = models.ForeignKey(Term)
    parent = models.ForeignKey('self')
    
    posts = models.ManyToManyField(Posts)
    
    name = models.CharField(max_length=48)
    descriptions = models.TextField()
    counter = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    lvl = models.IntegerField()
    root = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
   
    def __unicode__(self):
        return self.name