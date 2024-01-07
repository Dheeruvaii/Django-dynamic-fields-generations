from  rest_framework import serializers
from .models import Author
from rest_framework import generics
import datetime

class AuthorSerializers(serializers.ModelSerializer):
    age=serializers.SerializerMethodField()
    class Meta:
        model=Author
        fields=('id', 'name', 'dob', 'age')
        
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        age_data={
            'age':Author.age
        }
        representation['age']=age_data  
        return representation