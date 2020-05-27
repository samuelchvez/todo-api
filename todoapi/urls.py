from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

from users.views import UserViewSet
from todos.views import TodoListViewSet, TodoItemViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'todo-lists', TodoListViewSet)
router.register(r'todo-items', TodoItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/token-auth/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
    url(r'^api/v1/', include(router.urls)),
]
