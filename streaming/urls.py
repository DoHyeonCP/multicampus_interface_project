from django.urls import path

from . import views

app_name = 'streaming'

urlpatterns = [
    path('', views.video_list, name = 'list'),
    path('<int:video_id>', views.video_detail, name = 'detail'),
    path('video_upload/', views.video_upload, name = 'video_upload'),
] 