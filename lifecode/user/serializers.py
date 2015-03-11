'''
Created on Jan 26, 2015

@author: nunenuh
'''
from orm.users import User, UserProfile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id','displayName','username','email','password',
            'active','role', 'created','modified'
        )

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id','user','first_name','last_name','aboutme','birthdate','address',
            'city','state','country','zipcode','phone','created','modified'
        )
