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
