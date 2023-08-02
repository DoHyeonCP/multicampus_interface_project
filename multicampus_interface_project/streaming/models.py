from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200, default = '')
    videofile = models.FileField(null = True, upload_to ="", blank = True )
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes')
    view_count = models.IntegerField(default=0) # 조회수 필드



class Subscription(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # 생성된 시간 저장


