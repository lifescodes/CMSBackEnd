from django.shortcuts import render
from orm.media import MediaFile, MediaAlbum, MediaAlbumFile
from orm.users import User
from media.serializers import MediaFileSerializer, MediaAlbumSerializer, MediaAlbumFileSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework import views
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
import django_filters
# import filters

import os.path
from mimetypes import MimeTypes
import urllib
from random import randrange
from lifecode import settings
from media.helpers import MediaHelper
from PIL import Image



class FileUploadView(views.APIView):
    # parser_classes = (MultiPartParser, FormParser,)
    parser_classes = (FileUploadParser, )


    def post(self, request, format=None):
        reqfile = request.FILES['file']
        post = request.POST
        helper = MediaHelper()

        random = str(randrange(99999999999))

        upload_file_name = reqfile.name
        file_name_clean = helper.format_filename(upload_file_name) #clean from whitespace
        file_name = random + '_' + file_name_clean  #randomize filename
        file_size = reqfile.size

        #get file mime type
        mime = MimeTypes()
        url = urllib.pathname2url(file_name)
        mime_type = mime.guess_type(url)
        file_mime = mime_type[0]

        #get file extension
        ext = os.path.splitext(file_name);
        file_ext = ext[1]

        #get file type (image, audio, video, application, ...etc)
        mtype = file_mime.split('/')
        file_type = mtype[0]

        #get path and url

        file_path = helper.getPath(file_type)
        file_url = helper.getURL(file_type)

        #create directory for file
        if not os.path.isdir(file_path):
            os.makedirs(file_path, 0777)


        #save file to destination
        destination = open(file_path + file_name, 'wb+')
        for chunk in reqfile.chunks():
            destination.write(chunk)
            destination.close()

        #save file information to database
        mfile = MediaFile()
        mfile.name = upload_file_name
        mfile.file_name = file_name
        mfile.file_size = file_size
        mfile.file_ext = file_ext
        mfile.file_mime = file_mime
        mfile.file_type = file_type
        mfile.file_url = file_url

        user_id = post.get('user')
        user = User.objects.get(pk=user_id)
        mfile.user = user

        #crate thumbs if file is image
        if (file_type == "image"):
            thumb_file = random + '_thumbs'+file_ext
            image_path = os.path.join(file_path,file_name)
            thumb_path = os.path.join(file_path, thumb_file)
            thumb_size = [256,256]
            crop_type='middle'
            helper.resizeAndCrop(image_path, thumb_path, thumb_size, crop_type)
            mfile.thumb_file = thumb_file
            mfile.thumb_url = file_url
        elif (file_type=="video"):
            mfile.thumb_file = 'video_thumb.png'
            mfile.thumb_url = settings.base.UPLOAD_VIDEO_URL +'/'
        elif (file_type=="audio"):
            mfile.thumb_file = 'audio_thumb.png'
            mfile.thumb_url = settings.base.UPLOAD_AUDIO_URL +'/'
        else:
            mfile.thumb_file = 'other_thumb.png'
            mfile.thumb_url = settings.base.UPLOAD_OTHER_URL +'/'

        #get dimension
        if (file_type=="image"):
            image_path = os.path.join(file_path,file_name)
            img = Image.open(image_path)
            width, height = img.size
            mfile.dimension_width = width
            mfile.dimension_height = height

        mfile.save() #save to databases

        return Response(status=201)



class MediaFileFilter(django_filters.FilterSet):
    # manufacturer = django_filters.CharFilter(name="file_type__name")


    class Meta:
        model = MediaFile
        fields = ['file_type']

class MediaFileFilterList(generics.ListAPIView):
     queryset = MediaFile.objects.all()
     serializer_class = MediaFileSerializer
     filter_class = MediaFileFilter

    #  filter_backends = (filters.SearchFilter,)
    #  search_fields = ('file_type')



class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    filter_class = MediaFileFilter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=file_type')

    #delete override
    def destroy(self, request, pk=None):
        mfile = MediaFile.objects.filter(id=pk)
        if (mfile.exists()):
            mfile = MediaFile.objects.get(id=pk)

            base_path = settings.base.BASE_PATH

            url_path = mfile.file_url.split('/')
            upload_path = ''
            for strip in url_path:
                if strip != '':
                    upload_path = upload_path + strip + '/'

            file_name = mfile.file_name
            thumb_file = mfile.thumb_file

            file_path = os.path.join(base_path, upload_path, file_name)

            remove_status = False
            if os.path.exists(file_path):
                os.remove(file_path)
                remove_status = True

            if (mfile.file_type == "image"):
                thumbs_path = os.path.join(base_path, upload_path, thumb_file)
                os.remove(thumbs_path)

            #removing from database
            mfile.delete()

            if remove_status:
                return Response(status=204)
            else:
                out = {"detail": "Error File Already removed from Server"}
                return Response(out, status=404)

            # return Response(path_file_thumbs, status=204)

        else:
            out = {"detail": "Not found"}
            return Response(out, status=404)







class MediaAlbumViewSet(viewsets.ModelViewSet):
    queryset = MediaAlbum.objects.all()
    serializer_class = MediaAlbumSerializer

class MediaAlbumFileViewSet(viewsets.ModelViewSet):
    queryset = MediaAlbumFile.objects.all()
    serializer_class = MediaAlbumFileSerializer
