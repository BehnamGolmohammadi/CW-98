from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.AllTask.as_view() ,name= 'index'),
    # path('taskinfo/<int:task_id>', views.TaskDetail.as_view(), name='taskinfo'),
    path('taskinfo/<int:pk>', views.TaskDetailView.as_view(), name='taskinfo'),
    # path('newtask/', views.NewTask.as_view(), name='newtask'),
    path('newtask/', views.NewTaskView.as_view(), name='newtask'),
    # path('updatetask/<int:task_id>', views.UpdateTask.as_view(), name='updatetask'),
    path('updatetask/<int:pk>', views.UpdateTaskView.as_view(), name='updatetask'),
    path('deletetask/<int:task_id>', views.DeleteTask.as_view(), name='deletetask'),
]