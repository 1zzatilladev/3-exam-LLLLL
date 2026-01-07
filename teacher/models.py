from django.db import models
from users.models import User
# Create your models here.




class Teacher(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  courses = models.ManyToManyField('course.Cours', blank=True)
  experience_year = models.CharField(max_length=150)
  is_support = models.BooleanField(default=False)
  education = models.CharField(max_length=150)
  salary = models.DecimalField(max_digits=10, decimal_places=2)
  is_active = models.BooleanField(default=False)




  def __str__(self) -> str:
    return f"Teacher: {self.user.username}"
