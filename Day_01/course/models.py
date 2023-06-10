from django.db import models

# Create your models here.
class courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name= models.CharField(max_length=20)
    course_capacity=models.IntegerField(default=20)