from django.shortcuts import render, get_object_or_404
from .models import Task

# Create your views here.
def all_task(request):
    all_task = Task.objects.all().values()
    return render(request, 'task/task.html', context= {'all_task': all_task})

def task_detail(request, task_id):
       task = Task.objects.get(id=task_id)
       return render(request, 'task/task.html', {'single_task': task})