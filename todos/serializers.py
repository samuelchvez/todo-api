from rest_framework import serializers

from .models import TodoList, TodoItem


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = (
            'id',
            'created_by',
            'title',
        )


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = (
            'id',
            'belongs_to',
            'title',
            'priority',
            'due_date',
        )
