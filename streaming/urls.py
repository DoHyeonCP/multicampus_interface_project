from django.urls import path

from . import views
app_name = 'streaming'

urlpatterns = [
    path('', views.video_list, name = 'list'),
    path('<int:video_id>', views.video_detail, name = 'detail'),
    path('video_upload/', views.video_upload, name = 'video_upload'),
    path('video_modify/<int:video_id>', views.video_modify, name = 'video_modify'),
    path('video_delete/<int:video_id>', views.video_delete, name = 'video_delete')
]