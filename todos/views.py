from django.contrib.auth.models import User
from rest_framework import viewsets

from permissions.services import APIPermissionClassFactory
from .models import TodoList, TodoItem
from .serializers import TodoListSerializer, TodoItemSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TodoListPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': True,
                    'update': True,
                    'partial_update': True,
                }
            }
        ),
    )

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TodoItemPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': True,
                    'update': True,
                    'partial_update': True,
                }
            }
        ),
    )
