from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.all_task ,name= 'index'),
    path('taskinfo/<int:task_id>', views.task_detail, name='taskinfo'),
    path('newtask/', views.new_task, name='newtask'),
    path('updatetask/<int:task_id>', views.update_task, name='updatetask'),
    path('deletetask/<int:task_id>', views.delete_task, name='deletetask'),
]