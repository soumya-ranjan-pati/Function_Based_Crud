from django.db import models

# Create your models here.
class Employee(models.Model):
      idno=models.IntegerField(primary_key=True)
      name=models.CharField(max_length=70)
      contact=models.IntegerField()
      email=models.EmailField()
      salary=models.FloatField()
      address=models.TextField(blank=True)

