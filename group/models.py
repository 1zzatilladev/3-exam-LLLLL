from django.db import models
from teacher.models import Teacher
# Create your models here.




class Group(models.Model):
    course = models.ForeignKey('course.Cours', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)



class GroupLessonOpen(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey('course.Lesson', on_delete=models.CASCADE)  
    is_open = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name
