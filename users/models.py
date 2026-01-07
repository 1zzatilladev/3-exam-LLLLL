from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Regions(models.Model):
    name = models.CharField(max_length=233)
    is_active = models.BooleanField(default=False)

class Districts(models.Model):
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(max_length=233)
    is_active = models.BooleanField(default=False)

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'DR', 'admin'
        TEACHER = 'tch', 'teacher'
        STUDENT = 'ST', 'student'
        PARENT = 'PR', 'parent'
    class Gender(models.TextChoices):
        male = 'erkak', 'erkak'
        famali = 'ayol', 'ayol'
    name = models.CharField(max_length=233)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    mail = models.CharField(max_length=233, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    address = models.TextField(max_length=233)
    passport_seria = models.CharField(max_length=30)
    passport_image = models.ImageField(upload_to='passport/')
    groups = models.ManyToManyField('auth.Group', related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users', blank=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_posts')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_past_user_views')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class User_otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=233)
    attempt_count = models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)






