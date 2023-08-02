from django.urls import path

from . import views

urlpatterns = [
    path('', views.video_list, name = 'list'),
    path('<int:video_id>', views.video_detail, name = 'detail'),
    path('video_upload/', views.video_upload, name = 'video_upload'),
    path('video_modify/<int:video_id>', views.video_modify, name = 'video_modify'),
    path('video_delete/<int:video_id>', views.video_delete, name = 'video_delete'),
    path('video_likes/<int:video_id>', views.post_l, name='video_likes'),
    path('view_count/<int:video_id>',views.increment_view_count, name='video_viewcount'), 
]