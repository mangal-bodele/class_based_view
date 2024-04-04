from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    company = models.CharField(max_length=10)
    salary = models.IntegerField()
    date_of_Joining = models.DateField()
    city = models.CharField(max_length=10)
    mobile = models.IntegerField()
