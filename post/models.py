from django.db import models
from users.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_posts')
    title = models.CharField(max_length=233)
    descriptions = models.TextField(blank=True, null=True)
    viewers_count = models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post_hashtag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag = models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)

class Past_user_view(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_past_user_views')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
