from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField("설명", max_length=200, blank=True)
    content = models.TextField("본문")
    photo = models.ImageField(blank=True, null=True)
    create_date = models.DateTimeField("작성시간", auto_now_add=True)
    modify_date = models.DateTimeField("수정시간", auto_now=True)

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'

class PostImage(models.Model):
    property = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'
