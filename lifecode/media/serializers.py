'''
Created on Jan 26, 2015

@author: nunenuh
'''
from orm.users import User
from orm.media import MediaFile, MediaAlbum, MediaAlbumFile
from rest_framework import serializers

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = (
            'id','user','name','descriptions',
            'file_name','file_size','file_ext','file_mime',
            'file_type', 'file_url', 'thumb_file', 'thumb_url',
            'dimension_width','dimension_height',
            'created','modified','album'
        )

class MediaAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAlbum
        fields = (
            'id','name','descriptions','counter','created','modified','file'
        )

class MediaAlbumFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAlbumFile
        fields = (
            'id','album','file'
        )
