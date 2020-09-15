from django.db import models

# Create your models here.

class video_content(models.Model):
    video = models.FileField(upload_to='post', null=True)

