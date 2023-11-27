from django.shortcuts import render
from .models import Category, Notebook
# Create your views here.


def category(request):
    category_list = Category.objects.all()
    return render(request, 'category.html', context={
        'list_category':category_list
    })

def notebooks(request, slug):
    category_filter = Category.objects.filter(slug=slug)
    return render(request, 'notebooks.html', context={
        'category_filter':category_filter
    })