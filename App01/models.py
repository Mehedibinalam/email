from decimal import Decimal
from django.db import models

# Create your models here.

class Trainee(models.Model):
    TraineeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    BatchNo = models.CharField(max_length=15)
    ContactNo = models.CharField(max_length=15)
    ContactAddress = models.CharField(max_length=100)
    EmailAddress = models.EmailField()
    DueAmount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))

    class Meta:
        db_table = "Trainee"

class StudentID(models.Model):
    StudentID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    BatchNo = models.CharField(max_length=15)
    ContactNo = models.CharField(max_length=15)
    ContactAddress = models.CharField(max_length=100)
    EmailAddress = models.EmailField()

class EmployeeID(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    BatchNo = models.CharField(max_length=15)
    ContactNo = models.CharField(max_length=15)
    ContactAddress = models.CharField(max_length=100)
    EmailAddress = models.EmailField()