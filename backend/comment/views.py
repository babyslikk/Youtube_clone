from functools import partial
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializer import CommentSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes ([AllowAny])
def get_all_comment(request, id):
    comment = Comment.objects.filter(video_id=id)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes ([IsAuthenticated])
def new_comment (request):
    serializer = CommentSerializer (data=request.data)
    if serializer.is_valid():
        serializer.save (user=request.user)
        return Response (serializer.data, status=status.HTTP_201_CREATED)
    return Response (serializer.errors, status=status.HTTP_402_PAYMENT_REQUIRED)

#Getting "get () return more than one Comment -- it returned 3 intermediate django 20:30!"
@api_view(['PATCH'])
@permission_classes ([IsAuthenticated])
def likes(request, id):
    #comment = Comment.objects.filter(video_id=id, likes=0)

    type = request.query_params.get ('type')
    print (type)

    if type == 'likes':
        comment = Comment.objects.get (pk=id)

        data = {'likes': comment.likes + int(1) }
        serializer = CommentSerializer (comment, data=data, partial =True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status=status.HTTP_200_OK)
    
    elif type == 'dislikes':
        comment = Comment.objects.get (pk=id)

        data = {'dislikes': comment.dislikes +int(1)}
        serializer = CommentSerializer (comment, data=data, partial =True)
        serializer.is_valid (raise_exception=True)
        serializer.save()
        return Response (serializer.data, status=status.HTTP_200_OK)
