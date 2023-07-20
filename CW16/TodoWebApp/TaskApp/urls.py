from django.urls import path, include
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.all_task ,name= 'index'),
    path('taskinfo/<int:task_id>', views.task_detail, name='taskinfo')
]