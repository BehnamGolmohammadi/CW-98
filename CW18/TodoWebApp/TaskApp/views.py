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

      return render(request, 'task/task.html', {'new_task': 1, 'all_category': Category.objects.all(),
                                                 'all_tag': Tag.objects.all(),
                                                   'all_status':Task.status_choices
                                                   })

def update_task(request, task_id):
      if request.method == "POST":
            old_task = Task.objects.get(id=task_id)
            title = request.POST.get('title') or old_task.title
            category = Category.objects.get(id = request.POST.get('category')) or old_task.category
            description = request.POST.get('description') or old_task.description
            due_date = request.POST.get('due_date') or old_task.due_date
            status = request.POST.get('status') or old_task.status
            tag = request.POST.getlist('tag') or old_task.tag.all()

            print(old_task, title, category, description, due_date, status, tag)

            # Create the task object
            old_task = Task.objects.filter(id=task_id)
            old_task.update(
            title=title,
            category =category ,
            description=description,
            due_date=due_date,
            status=status,
            )

            tag_list = []
            for each_tag in tag:
                  tag_obj = Tag.objects.get(id = each_tag)
                  tag_list.append(tag_obj)
            
            old_task.first().tag.set(tag_list)
            old_task.first().save()

            return redirect("/")

      return render(request, 'task/task.html', {'update_task': 1,
                                                'all_category': Category.objects.all(),
                                                'all_tag': Tag.objects.all(),
                                                'all_status':Task.status_choices,
                                                'task_id': task_id 
                                                     })


def delete_task(request, task_id):
            
      Task.objects.get(id=task_id).delete()
      return redirect("/tasks")


