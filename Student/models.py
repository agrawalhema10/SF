from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Create your models here.
class Student(models.Model):
    STATUS=(('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'))
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    college_name=models.CharField(max_length=200,null=True)
    passout_year=models.CharField(max_length=200,null=True,choices=STATUS)
    phone=models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=5, null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name