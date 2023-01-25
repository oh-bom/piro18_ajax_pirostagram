from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    like=models.IntegerField()
    comment=models.TextField(null=True, blank=True)
