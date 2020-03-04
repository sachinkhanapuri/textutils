from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=20)
    emailid=models.CharField(max_length=20)
    contactno=models.CharField(max_length=10)
    gender=models.CharField(max_length=20)

    def __str__(self):
        return self.name