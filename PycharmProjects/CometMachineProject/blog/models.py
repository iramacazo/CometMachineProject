from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_time = models.DateTimeField(default=datetime.now)
    post_title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=300)

    def __str__(self):
        return 'Post: {}: {}'.format(self.author, self.post_title)
