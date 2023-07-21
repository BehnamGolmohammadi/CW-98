from django.shortcuts import render
from .models import Task
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def all_task(request):
    all_task = Task.objects.all()
    pg = Paginator(all_task, 5)
    page_number = request.GET.get('page')
    try:
          page_obj = pg.get_page(page_number)
    except PageNotAnInteger:
          page_obj = pg.page(1)
    except EmptyPage:
          page_obj = pg.page(pg.num_pages)

    
          

    return render(request, 'task/task.html', context= {'page_obj': page_obj})


def task_detail(request, task_id):
       task = Task.objects.get(id=task_id)
       return render(request, 'task/task.html', {'single_task': task})