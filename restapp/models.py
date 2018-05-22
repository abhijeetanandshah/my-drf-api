from django.db import models
# Create your models here.


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, default=0)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    branch = models.CharField(max_length=10)
    college_name = models.CharField(max_length=30)