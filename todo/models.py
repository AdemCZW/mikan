from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Todo(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='name')
    finish = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now)


# Create your models here.  
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
 
    def __str__(self):
        return self.firstname + " " + self.lastname
  
    class Meta:  
        db_table = "web_member"


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    tel = models.IntegerField()
    password = models.CharField(max_length=20, blank=False, null=True)    

class Flight(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    items = models.CharField(max_length=10, default=" ")
    fromname = models.CharField(max_length=10)
    arrivalname = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    finish = models.BooleanField(default=False)
    pub_date = models.DateTimeField(null=True)
    
    