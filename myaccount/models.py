from django.db import models

# Create your models here.
class trainee_info(models.Model):
    trainee_name= models.CharField(max_length=20)
    trainee_email=models.EmailField(max_length=100)
    password = models.CharField(max_length=16)
    is_activ =models.BooleanField(default=True)

