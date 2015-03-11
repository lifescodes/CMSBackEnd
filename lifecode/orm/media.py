'''
Created on Feb 17, 2015

@author: nunenuh
'''

from django.db import models
from orm.users import User

class MediaFile(models.Model):
    user = models.ForeignKey(User)

    name = models.TextField()
    descriptions = models.TextField()
    file_name = models.TextField()
    file_size = models.TextField()
    file_ext = models.CharField(max_length=255)
    file_mime = models.CharField(max_length=255)
    file_type = models.CharField(max_length=45)
    file_url = models.TextField()
    thumb_file = models.TextField(default=None, null=True, blank=True)
    thumb_url = models.TextField(default=None, null=True, blank=True)
    dimension_width = models.CharField(max_length=45, default=None, null=True, blank=True)
    dimension_height = models.CharField(max_length=45, default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_file'

    def __unicode__(self):
        return self.name

class MediaAlbum(models.Model):
    file = models.ManyToManyField(
        MediaFile,
        through="MediaAlbumFile",
        through_fields=('album', 'file'),
        related_name="album"
    )

    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    counter = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'media_album'

    def __unicode__(self):
        return self.name

class MediaAlbumFile(models.Model):
    file = models.ForeignKey(MediaFile, db_column="file_id")
    album = models.ForeignKey(MediaAlbum, db_column="album_id")

    class Meta:
        db_table = 'media_album_file'
