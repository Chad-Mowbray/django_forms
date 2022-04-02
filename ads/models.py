from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()