from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from django.db import models
from .models import Like

def mainpage(request):
    return render(request, 'Landingpage.html')

def auth(request):
    return render(request, 'auth.html')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    views = models.PositiveBigIntegerField(default=0)

def post_m(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'video.html', {'post':post})

def post_l(request, pk):
    post = get_object_or_404(Like, pk=pk)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('video.html', post_id=post_id)