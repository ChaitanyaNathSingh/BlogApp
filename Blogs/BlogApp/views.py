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
        p = Post.objects.all()
        post_serializers = PostSerializers(p, many=True)
        return Response(post_serializers.data, status=status.HTTP_200_OK)
    else:
        post_serializers = PostSerializers(data=request.data)
        post_serializers.is_valid(raise_exception=True)
        post_serializers.save()
        return Response(post_serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def posts_update(request, pk):
    p = get_object_or_404(Post, id=pk)
    if request.method == "GET":
        post_serializers = PostSerializers(p)
        return Response(post_serializers.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        post_serializers = PostSerializers(instance=p, data=request.data)
        post_serializers.is_valid(raise_exception=True)
        post_serializers.save()
        return Response(post_serializers.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        p.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]