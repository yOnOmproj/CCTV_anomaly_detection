from django.db import models

# Create your models here.

class video_content(models.Model):
    video = models.FileField(upload_to='post', null=True)
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


class mat(models.Model):
    title = models.CharField(max_length=50, null=True)
    mat = models.FileField(upload_to='mat', null=True)

    def __str__(self):
        return self.title

