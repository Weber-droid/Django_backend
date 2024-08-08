from django.db import models

# Create your models here.

class Students(models.Model):
    firstName = models.CharField(max_length=100)
    surName = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"First Name: {self.firstName}, Surname: {self.surName} and Email: {self.Email}."
