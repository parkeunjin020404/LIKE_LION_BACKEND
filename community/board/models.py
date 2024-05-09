from django.db import models
from accounts.models import CustomUser


class Community(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
  
    post = models.ForeignKey(Community,null=False, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=200)

    

# Create your models here.
