from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.conf import settings
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]
    
class Comment (models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE, null=True,related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return (self.author.username if self.author else "무명") + "의 댓글"

