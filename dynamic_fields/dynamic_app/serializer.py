from  rest_framework import serializers
from .models import Author
from rest_framework import generics
import datetime

class AuthorSerializer(serializers.ModelSerializer):
    dynamic_fields = serializers.JSONField(default=dict, required=False)

    class Meta:
        model = Author
        fields = ['id', 'name', 'dob', 'dynamic_fields']
        read_only_fields = ['id']

    def create(self, validated_data):
        dynamic_fields_data = validated_data.pop('dynamic_fields', {})
        author = Author.objects.create(**validated_data)
        author.dynamic_fields = dynamic_fields_data
        author.save()
        return author

    def update(self, instance, validated_data):
        dynamic_fields_data = validated_data.pop('dynamic_fields', {})
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.dynamic_fields = dynamic_fields_data
        instance.save()
        return instance
        