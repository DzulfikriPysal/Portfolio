from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    context = {}
    return render(request, 'blog/blog.html', context)

def single_blog(request):
    context = {}
    return render(request, 'blog/single_blog.html', context)
