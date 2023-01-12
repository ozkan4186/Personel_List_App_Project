from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    Department_number = models.CharField(max_length=10)
    Department_name = models.CharField(max_length=15)
    staff_work = models.IntegerField()
   
   
   
    
    def __str__(self):
        return f'{self.Department_number} - {self.Department_name} - {self.staff_work}'



class Personal(models.Model):
    Personal_number = models.IntegerField()
    Did_jined=models.CharField(max_length=20)
    Title = models.CharField(max_length=300)       
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    Gender= models.CharField(max_length=15)
    Salary=models.IntegerField()
   
    
  

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Personalite(models.Model):         #(cooper - murat)  - (cooper - jason) - () ....
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Personal = models.ManyToManyField(Personal, related_name="reservations")
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="reservation")
    