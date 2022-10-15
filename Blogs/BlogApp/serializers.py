from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'genre', 'description', 'publish_date')