from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Index_001(models.Model):
    mid_001 = models.CharField(max_length=10)
    mid_ph_001 = models.CharField(max_length=1000,null=True)
    mid_txt_001 = models.TextField(max_length=100)
    mid_002 = models.CharField(max_length=10)
    mid_ph_002 = models.CharField(max_length=1000,null=True)
    mid_txt_002 = models.TextField(max_length=100)
    mid_003 = models.CharField(max_length=10)
    mid_ph_003 = models.CharField(max_length=1000,null=True)
    mid_txt_003 = models.TextField(max_length=100)
    mid_004 = models.CharField(max_length=10)
    mid_txt_004 = models.TextField(max_length=100)
    mid_ph_004 = models.CharField(max_length=1000,null=True)
    mid_005 = models.CharField(max_length=10)
    mid_txt_005 = models.TextField(max_length=100)
    mid_ph_005 = models.CharField(max_length=1000,null=True)
    mid_006 = models.CharField(max_length=10)
    mid_txt_006 = models.TextField(max_length=100)
    mid_ph_006 = models.CharField(max_length=1000,null=True)


class Studio_001(models.Model):
    studio_ph_001 = models.CharField(max_length=1000,default='圖片連結')

class Service_001(models.Model):
    service_ph_001 = models.CharField(max_length=1000,default='圖片連結')    

class Price_001(models.Model):
    price_btn_001 = models.CharField(max_length=1000,default='按鈕名稱') 
    price_txt_001 = RichTextField(max_length=1000,default='輸入文字敘述',blank=True, null=True) 

class Price_002(models.Model):
    price_btn_002 = models.CharField(max_length=1000,default='按鈕名稱') 
    price_txt_002 = RichTextField(max_length=1000,default='輸入文字敘述',blank=True, null=True)           

class Price_003(models.Model):
    price_btn_003 = models.CharField(max_length=1000,default='按鈕名稱') 
    price_txt_003 = RichTextField(max_length=1000,default='輸入文字敘述',blank=True, null=True)           

class Price_004(models.Model):
    price_btn_004 = models.CharField(max_length=1000,default='按鈕名稱') 
    price_txt_004 = RichTextField(max_length=1000,default='輸入文字敘述',blank=True, null=True)           

class Pn_001(models.Model):
    pn_ph_001 = models.CharField(max_length=1000,default='圖片連結')

class Pf_001(models.Model):
    pf_ph_001 = models.CharField(max_length=1000,default='圖片連結')

class Cp_001(models.Model):
    cp_ph_001 = models.CharField(max_length=1000,default='圖片連結')  

class Sg_001(models.Model):
    sg_ph_001 = models.CharField(max_length=1000,default='圖片連結')

class Pt_001(models.Model):
    pt_ph_001 = models.CharField(max_length=1000,default='圖片連結')

class at_001(models.Model):
    at_tit_001 = models.CharField(max_length=1000,default='標題')
    at_ph_001 = models.CharField(max_length=1000,default='活動圖照')
    at_con_001 = RichTextField(max_length=1000,default='活動內容',blank=True, null=True)

class Wedding_01(models.Model):
    Wedding_ph_001 = models.CharField(max_length=1000,default='圖片連結')

class Wedding_02(models.Model):
    Wedding_02_ph_001 = models.CharField(max_length=1000,default='圖片連結')

class Wedding_03(models.Model):
    Wedding_03_ph_001 = models.CharField(max_length=1000,default='圖片連結')

class Wedding_04(models.Model):
    Wedding_04_ph_001 = models.CharField(max_length=1000,default='圖片連結')  
          
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
    pub_date = models.DateTimeField(null=True,auto_now=True)
    pd_content = RichTextField(blank=True, null=True)

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




