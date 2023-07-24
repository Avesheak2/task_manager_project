from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.create_task, name='create_task'),
]
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

@api_view(['GET'])
def get_user_info(request, user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
from django.contrib.auth.models import Group, Permission
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment, Task
from .serializers import CommentSerializer

@api_view(['POST'])
def add_comment(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task=task)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_comments(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    comments = task.comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def update_delete_comment(request, task_id, comment_id):
    try:
        task = Task.objects.get(pk=task_id)
        comment = task.comments.get(pk=comment_id)
    except Task.DoesNotExist:
        return Response({"error": "Task or Comment not found"}, status=404)
    except Comment.DoesNotExist:
        return Response({"error": "Comment not found"}, status=404)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({"message": "Comment deleted successfully"}, status=204)
