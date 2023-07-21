from django.shortcuts import render
from TaskApp.models import Task, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# Create your views here.
def all_category(request):
    all_category = Category.objects.all()

    pg = Paginator(all_category, 5)
    page_number = request.GET.get('page')
    try:
          page_obj = pg.get_page(page_number)
    except PageNotAnInteger:
          page_obj = pg.page(1)
    except EmptyPage:
          page_obj = pg.page(pg.num_pages)

    return render(request, 'category/category.html', context= {'page_obj': page_obj})

def category_detail(request, cat_id):
    category = Category.objects.get(id=cat_id)
    return render(request, 'category/category.html', {'single_category': category})