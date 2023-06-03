from django.db import models

# Create your models here.
class trainee_list(models.Model):
    id=models.AutoField(primary_key=True)
    trainee_name= models.CharField(max_length=20)
    trainee_email=models.EmailField(max_length=100)
