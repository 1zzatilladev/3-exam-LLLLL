from django.db import models
from users.models import User
from teacher.models import Teacher
# Create your models here.
class CourseCategory(models.Model):
    category_name = models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)

class Cours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cours_cat = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=233)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='cours/')
    is_active = models.BooleanField(default=False)
    max_st = models.IntegerField(default=12, null=False)
    cours_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_st_count = models.CharField(max_length=233)
    now_st_count = models.CharField(max_length=233)
    finish_st = models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Coursescheduleweek_days(models.Model):
    name_uz = models.CharField(max_length=233)
    name_uzkr = models.CharField(max_length=233)
    name_ru = models.CharField(max_length=233)
    name_en = models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)

class Courseschedule(models.Model):
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE)
    group = models.CharField(max_length=233, blank=True, null=True)
    day_of_week = models.ManyToManyField(Coursescheduleweek_days)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    room = models.CharField(max_length=233)
    note = models.CharField(max_length=233)

class LessonModule(models.Model):
    course=models.ForeignKey(Cours,on_delete=models.CASCADE)
    module_number=models.CharField(max_length=233)
    title=models.CharField(max_length=233)
    description=models.CharField(max_length=233,blank=True,null=True)
    image = models.ImageField(upload_to='media/')
    files = models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)

class Lesson(models.Model):
    lesson_modul = models.ForeignKey(LessonModule,on_delete=models.CASCADE)
    lesson_number = models.CharField(max_length=23)
    title=models.CharField(max_length=233)
    description=models.CharField(max_length=233,blank=True,null=True)
    image = models.ImageField(upload_to='media/')
    files = models.CharField(max_length=233)
    is_exam = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Homework(models.Model):
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title=models.CharField(max_length=233)
    description=models.CharField(max_length=233,blank=True,null=True)
    image = models.ImageField(upload_to='media/')
    files = models.CharField(max_length=233)
    is_exam = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StudentsHomework(models.Model):
    homework = models.ForeignKey(Homework,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    comment=models.CharField(max_length=233)
    ai_feedback = models.CharField(max_length=300)
    is_teacher_checked = models.BooleanField(default=False)
    teacher_star = models.CharField(max_length=233)
    add_coin = models.CharField(max_length=233)
    files = models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StudentsAttance(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    group= models.ForeignKey('group.Group',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student = models.ForeignKey('student.Student',on_delete=models.CASCADE)
    is_student_here=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class LessonQuession(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title=models.CharField(max_length=233)
    description=models.CharField(max_length=233,blank=True,null=True)
    is_active=models.BooleanField(default=False)
    duration =models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LessonQuessionsQuession(models.Model):
    lesson_quession = models . ForeignKey(LessonQuession,on_delete=models.CASCADE)
    title=models.CharField(max_length=233)
    description=models.CharField(max_length=233,blank=True,null=True)
    is_active=models.BooleanField(default=False)
    duration =models.CharField(max_length=233)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class StudentRate(models.Model):
    student = models.ForeignKey('student.Student',on_delete=models.CASCADE)
    question = models.ForeignKey(LessonQuession,on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=233)
    spent_time = models.DurationField()
    is_first_time = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

class QuestionsAnswer(models.Model):
    lesson_questions_quesrion = models . ForeignKey(LessonQuessionsQuession,on_delete=models.CASCADE)
    title=models.CharField(max_length=233)
    image = models.ImageField(upload_to='media/',blank=True)
    is_active=models.BooleanField(default=False)
    is_true=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
