from django.db import models
from account.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Post(BaseModel):
    image = models.ImageField()
    caption = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes_user')


class Comment(BaseModel):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    contents = models.TextField()
