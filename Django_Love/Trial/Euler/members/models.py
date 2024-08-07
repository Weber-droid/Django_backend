from django.db import models

# Create your models here.

class Students(models.Model):
    firstName = models.CharField(max_length=255),
    SurName = models.CharField(max_length=255),
    Nickname = models.CharField(max_length=255),
    #Email = models.EmailField
    #Password = models.
    
    def __str__(self):
        return self.firstName
    
class Course(models.Model):
    courseName = models.CharField(max_length=255),
    
    def __str__(self):
        return self.courseName
    
class Stud(models.Model):
    name = models.CharField(max_length=100),
    nicky = models.CharField(max_length=100),
    nanny = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name