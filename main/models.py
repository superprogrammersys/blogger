from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=250)
    body=models.TextField()
    user=models.ForeignKey(User,models.CASCADE,related_name="user")
    publish_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class comment(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User,models.CASCADE)
    post=models.ForeignKey(post,models.CASCADE,related_name="comments")
    publish_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content