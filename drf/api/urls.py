from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='Overview'),
    path('todo-list/', views.TodoList, name='TodoList'),
    path('todo-detail/<str:pk>/', views.TodoDetailView, name='TodoDetailView'),
    path('todo-create/', views.TodoCreate, name='TodoCreate'),
    path('todo-update/<str:pk>/', views.TodoUpdate, name='TodoUpdate'),
    path('todo-delete/<str:pk>', views.TodoDelete, name='TodoDelete'),
]
