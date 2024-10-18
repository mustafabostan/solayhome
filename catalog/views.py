from django.shortcuts import render
from catalog.models import Category,Post,Images


def index(request):
    context = {
        "posts":Post.objects.filter(is_active=True,is_home=True),
        "categories":Category.objects.all()
    }
    return render(request, "catalog/index.html",context)


def posts(request):
    context = {
        "posts":Post.objects.filter(is_active=True),
        "categories" : Category.objects.all(),              
    }
    return render(request, "catalog/posts.html",context)


def post_details(request, slug):
    context = {
        "post":Post.objects.get(slug=slug),
        "images":Images.objects.filter(post__slug=slug)                
    }
    return render(request, "catalog/post-details.html",context)


def post_by_category(request, slug):
    context = {
        "posts":Category.objects.get(slug=slug).post_set.filter(is_active=True),        
        "categories": Category.objects.all(),
        "selected_category":slug        
    }
    return render(request, "catalog/posts.html",context)

