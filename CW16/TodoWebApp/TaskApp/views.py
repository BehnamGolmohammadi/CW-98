from django.shortcuts import render, redirect
from .models import Task, Tag, Category
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


def new_task(request):
      if request.method == "POST":
            title = request.POST.get('title')
            category = request.POST.get('category')
            description = request.POST.get('description')
            due_date = request.POST.get('due_date')
            status = request.POST.get('status')
            tag = request.POST.getlist('tag')

            # Create the task object
            task = Task.objects.create(
            title=title,
            category =Category.objects.get(id = category),
            description=description,
            due_date=due_date,
            status=status,
            )
            print(tag)
            for each_tag in tag:
                  tag_obj = Tag.objects.get(id = each_tag)
                  task.tag.add(tag_obj)
            task.save()

            return redirect("/")

      return render(request, 'task/task.html', {'new_task': 1, 'all_category': Category.objects.all(), 'all_tag': Tag.objects.all(), 'all_status':Task.status_choices})