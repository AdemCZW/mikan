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
    items_choices = (
        ('tops', '衣服'),('pants','褲子'),('shoes','鞋子'),('accessories','配件'),('maintenance','保養品'),('makeup','化妝品'),
    )
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    items = models.CharField(max_length=20, choices=items_choices)
    fromname = models.CharField(max_length=10)
    arrivalname = models.CharField(max_length=50)
    pd_number = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100)
    finish = models.BooleanField(default=False)
    pub_date = models.DateTimeField(null=True)
    pd_content = models.CharField(max_length=1000,null=True)

    
    
class Movie(models.Model):
    GENRE_CHOICES = (
        ('action', '動作片'),
        ('romance', '愛情片'),
        ('drama', '劇情片'),
    )
    title = models.CharField(max_length=100)  # 電影名稱
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)  # 電影類型
    release_year = models.IntegerField()  # 年份    