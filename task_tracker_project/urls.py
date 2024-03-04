from django.contrib import admin
from django.urls import path
from task_tracker.views import task_list, create_task, edit_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
