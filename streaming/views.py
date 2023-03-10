from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count

def mainpage(request):
    return render(request, 'Landingpage.html')
