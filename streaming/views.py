from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from django.db import models

def mainpage(request):
    return render(request, 'Landingpage.html')

def auth(request):
    return render(request, 'auth.html')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    views = models.PositiveBigIntegerField(default=0)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, '#.html', {'post':post})