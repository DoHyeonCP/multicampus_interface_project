from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length = 200, default = '')
    videofile = models.FileField(null = True, upload_to ="", blank = True )
    
