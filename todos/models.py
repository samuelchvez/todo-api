from django.db import models
from django.conf import settings



class TodoList(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.TextField(null=True, blank=True)


class TodoItem(models.Model):
    belongs_to = models.ForeignKey(
        TodoList,
        on_delete=models.CASCADE,
    )
    title = models.TextField(null=True, blank=True)
    priority = models.PositiveIntegerField(default=0)
    due_date = models.DateField()
