from  rest_framework import serializers
from .models import Author
from rest_framework import generics

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=('id','name','dob','age')