from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : 'todo-list/',
        'Detail View' : 'todo-detail/<str:pk>/',
        'Create' : 'todo-create/',
        'Update' : 'todo-update/<str:pk>/',
        'Delete' : 'todo-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def TodoList(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TodoDetailView(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TodoCreate(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def TodoUpdate(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def TodoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response('Item Deleted Successfully')