from django.db import models

# Create your models here.
from users.models import User
from teacher.models import Teacher
from group.models import Group

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='students_as_user')
    course_category = models.ForeignKey('course.CourseCategory',on_delete=models.CASCADE)
    parent = models.ForeignKey(User,on_delete=models.CASCADE, related_name='students_as_parent')
    domain = models.CharField(max_length=344)
    status = models.CharField(max_length=233)
    coin = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CoinCategory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    coin = models.IntegerField()
    comment = models.CharField(max_length=233)
    class Status(models.TextChoices):
        INCREASE='increase','Kotarilish'
        DECREASE='decrease','Tushish'
    status=models.CharField(max_length=233,choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StudentCoinAction(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    coin_category=models.ForeignKey(CoinCategory,on_delete=models.CASCADE)
    comment=models.CharField(max_length=233,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StudentStopped(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    comment=models.CharField(max_length=233,blank=True)
    start_stopped=models.CharField(max_length=233)
    end_stopped=models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class StudentPaymentHistory(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    administrator=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    quantity=models.IntegerField()
    class PayWith(models.TextChoices):
        CASH='cash','Naqt'
        CART='cart','Karta'
        CLICK='click','Click'

    pay_with = models.CharField(max_length=23,choices=PayWith.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class StudentGroup(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    added_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    is_stopped=models.BooleanField(default=False)
