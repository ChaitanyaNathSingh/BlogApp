from .models import Post
from .serializers import PostSerializers
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET', 'POST'])
def posts_create(request):
    if request.method == "GET":
        """

        Write your code to list all the POSTS here and send response status , data
        Model Name = Post
        Serializer Class = PostSerializers

        """
        # p = Post.objects.all()
        # post_serializers = PostSerializers(p, many=True)
        # return Response(post_serializers.data, status=status.HTTP_200_OK)
    else:
        """

        Write your code to post a new POST here and send response status , data
        Model Name = Post
        Serializer Class = PostSerializers

        """
        # post_serializers = PostSerializers(data=request.data)
        # post_serializers.is_valid(raise_exception=True)
        # post_serializers.save()
        # return Response(post_serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def posts_update(request, pk):
    p = get_object_or_404(Post, title=pk)
    if request.method == "GET":
        """

        Write your code to get a single POST here and send response status , data
        Model Name = Post
        Serializer Class = PostSerializers

        """
        # post_serializers = PostSerializers(p)
        # return Response(post_serializers.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        """

        Write your code to update data of single POST here and send response status , data
        Model Name = Post
        Serializer Class = PostSerializers

        """
        # post_serializers = PostSerializers(instance=p, data=request.data)
        # post_serializers.is_valid(raise_exception=True)
        # post_serializers.save()
        # return Response(post_serializers.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        """

        Write your code to delete a single POST here and send response status , data
        Model Name = Post
        Serializer Class = PostSerializers

        """
        # p.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def filter_posts_author(request, pk):
    if request.method == "GET":
        """
        
        Write your code to filter POSTS by author here and send response status , data
        Model Name = Post
        Serializer Class = PostSerializers

        """
        # p = Post.objects.filter(author=pk)
        # post_serializers = PostSerializers(p, many=True)
        # return Response(post_serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filter_posts_genre(request, pk):
    if request.method == "GET":
        """
        
        Write your code to filter POSTS by genre here and send response status , data
        Model Name = Post
        Serializer Class = PostSerializers

        """
        # p = Post.objects.filter(genre=pk)
        # post_serializers = PostSerializers(p, many=True)
        # return Response(post_serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filter_posts_between_dates(request, start, end):
    if request.method == "GET":
        """
        
        Write your code to filter POSTS between dates here and send response status , data
        Model Name = Post
        Serializer Class = PostSerializers

        """
        # p = Post.objects.filter(date__range=[start, end])
        # post_serializers = PostSerializers(p, many=True)
        # return Response(post_serializers.data, status=status.HTTP_200_OK)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]