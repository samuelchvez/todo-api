from django.contrib.auth.models import User
from rest_framework import viewsets

from permissions.services import APIPermissionClassFactory
from .models import TodoList, TodoItem
from .serializers import TodoListSerializer, TodoItemSerializer


def is_authenticated(usr, req):
    return usr.is_authenticated

def todo_list_list_perm(usr, req):
    return req.GET.get('created_by', None) == str(usr.pk)

def todo_list_created_by_myself(usr, obj, req):
    return usr == obj.created_by


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    filter_fields = ('created_by',)
    permission_classes = (
        APIPermissionClassFactory(
            name='TodoListPermission',
            permission_configuration={
                'base': {
                    'create': is_authenticated,
                    'list': todo_list_list_perm,
                },
                'instance': {
                    'retrieve': todo_list_created_by_myself,
                    'destroy': todo_list_created_by_myself,
                    'update': todo_list_created_by_myself,
                    'partial_update': todo_list_created_by_myself,
                }
            }
        ),
    )


def todo_item_create_perm(usr, req):
    belongs_to_pk = int(req.data.get('belongs_to', -1))
    try:
        belongs_to = TodoList.objects.get(pk=belongs_to_pk)
        return usr == belongs_to.created_by
    except:
        return False


def todo_item_list_perm(usr, req):
    belongs_to_pk = int(req.GET.get('belongs_to', -1))
    try:
        belongs_to = TodoList.objects.get(pk=belongs_to_pk)
        return usr == belongs_to.created_by
    except:
        return False

def todo_item_one_of_mine_perm(usr, obj, req):
    return obj.belongs_to.created_by == usr


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    filter_fields = ('belongs_to',)
    permission_classes = (
        APIPermissionClassFactory(
            name='TodoItemPermission',
            permission_configuration={
                'base': {
                    'create': todo_item_create_perm,
                    'list': todo_item_list_perm,
                },
                'instance': {
                    'retrieve': todo_item_one_of_mine_perm,
                    'destroy': todo_item_one_of_mine_perm,
                    'update': todo_item_one_of_mine_perm,
                    'partial_update': todo_item_one_of_mine_perm,
                }
            }
        ),
    )
