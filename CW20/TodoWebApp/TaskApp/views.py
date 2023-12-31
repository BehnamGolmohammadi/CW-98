from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Task, Tag, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .mixin import TodoOwnerRequiredMixin as TORM, AllTodoOwnerRequiredMixin as ATORM

# Create your views here.
class AllTask(ATORM, View):
      def get(self, request):
            all_task = self.Tasks
            pg = Paginator(all_task, 5)
            page_number = request.GET.get('page')
            try:
                  page_obj = pg.get_page(page_number)
            except PageNotAnInteger:
                  page_obj = pg.page(1)
            except EmptyPage:
                  page_obj = pg.page(pg.num_pages)
            
            return render(request, 'task/task.html', context= {'page_obj': page_obj})

# class TaskDetail(TORM, View):
#       def get(self, request, task_id):
#             task = Task.objects.get(id=task_id)
#             return render(request, 'task/task.html', {'single_task': task})

class TaskDetailView(TORM, DetailView):
      model = Task
      template_name = 'task/task.html'
      context_object_name = 'single_task'

      
# class NewTask(View):
#       def post(self, request):
#             if request.method == "POST":
#                   title = request.POST.get('title')
#                   category = request.POST.get('category')
#                   description = request.POST.get('description')
#                   due_date = request.POST.get('due_date')
#                   status = request.POST.get('status')
#                   tag = request.POST.getlist('tag')
#                   author = request.user

#                   # Create the task object
#                   task = Task.objects.create(
#                   title=title,
#                   category =Category.objects.get(id = category),
#                   description=description,
#                   due_date=due_date,
#                   status=status,
#                   author = author
#                   )
#                   print(tag)
#                   for each_tag in tag:
#                         tag_obj = Tag.objects.get(id = each_tag)
#                         task.tag.add(tag_obj)
#                   task.save()

#                   return redirect("/")

#       def get(self, request):
#             return render(request, 'task/task.html', {'new_task': 1, 'all_category': Category.objects.all(),
#                                                       'all_tag': Tag.objects.all(),
#                                                       'all_status':Task.status_choices
#                                                       })
      
class NewTaskView(CreateView):
      model = Task
      template_name = 'task/task.html'
      fields = ['title', 'category', 'description', 'due_date', 'status', 'tag']
      success_url = reverse_lazy('home:index')
      
      def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
      
      def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context['new_task'] = 1
            context['all_category'] = Category.objects.all()
            context['all_tag'] = Tag.objects.all()
            context['all_status'] = Task.status_choices
            return context

# class UpdateTask(TORM, View):
#       def get(self, request, task_id):
#             return render(request, 'task/task.html', {'update_task': 1,
#                                                       'all_category': Category.objects.all(),
#                                                       'all_tag': Tag.objects.all(),
#                                                       'all_status':Task.status_choices,
#                                                       'task_id': task_id 
#                                                            })
      
#       def post(self, request, task_id):
#             old_task = Task.objects.get(id=task_id)
#             title = request.POST.get('title') or old_task.title
#             category = Category.objects.get(id = request.POST.get('category')) or old_task.category
#             description = request.POST.get('description') or old_task.description
#             due_date = request.POST.get('due_date') or old_task.due_date
#             status = request.POST.get('status') or old_task.status
#             tag = request.POST.getlist('tag') or old_task.tag.all()

#             print(old_task, title, category, description, due_date, status, tag)

#             # Create the task object
#             old_task = Task.objects.filter(id=task_id)
#             old_task.update(
#             title=title,
#             category =category ,
#             description=description,
#             due_date=due_date,
#             status=status,
#             )

#             tag_list = []
#             for each_tag in tag:
#                   tag_obj = Tag.objects.get(id = each_tag)
#                   tag_list.append(tag_obj)
            
#             old_task.first().tag.set(tag_list)
#             old_task.first().save()

#             return redirect("/")

class UpdateTaskView(TORM, UpdateView):
      model = Task
      template_name = 'task/task.html'
      fields = ['title', 'category', 'description', 'due_date', 'status', 'tag']
      
      def get_success_url(self) -> str:
            return reverse_lazy('task:taskinfo', kwargs={'pk': self.kwargs['pk']})

      def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
      
      def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context['update_task'] = 1
            context['all_category'] = Category.objects.all()
            context['all_tag'] = Tag.objects.all()
            context['all_status'] = Task.status_choices
            context['task_id'] = self.kwargs['pk']
            return context

class DeleteTask(View):
      def get(self, request, task_id):
            Task.objects.get(id=task_id).delete()
            return redirect("/tasks")


