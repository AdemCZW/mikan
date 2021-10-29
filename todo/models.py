from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Index_001(models.Model):
    mid_001 = models.CharField(max_length=10,verbose_name = '標題名稱')
    mid_ph_001 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結')
    mid_txt_001 = models.TextField(max_length=100,verbose_name = '內容')
    mid_002 = models.CharField(max_length=10,verbose_name = '標題名稱')
    mid_ph_002 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結')
    mid_txt_002 = models.TextField(max_length=100,verbose_name = '內容')
    mid_003 = models.CharField(max_length=10,verbose_name = '標題名稱')
    mid_ph_003 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結')
    mid_txt_003 = models.TextField(max_length=100,verbose_name = '內容')
    mid_004 = models.CharField(max_length=10,verbose_name = '標題名稱')
    mid_txt_004 = models.TextField(max_length=100,verbose_name = '內容')
    mid_ph_004 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結')
    mid_005 = models.CharField(max_length=10,verbose_name = '標題名稱')
    mid_txt_005 = models.TextField(max_length=100,verbose_name = '內容')
    mid_ph_005 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結')
    mid_006 = models.CharField(max_length=10,verbose_name = '標題名稱')
    mid_txt_006 = models.TextField(max_length=100,verbose_name = '內容')
    mid_ph_006 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結')

    def __str__(self):
        return "首頁編輯" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '首頁'
        verbose_name = '首頁'

class Studio_001(models.Model):
    studio_ph_001 = models.CharField(max_length=1000,default='',verbose_name = '照片連結')

    def __str__(self):
        return "照片連結" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '攝影棚圖片'
        verbose_name = '攝影棚圖片'

class Service_001(models.Model):
    service_ph_001 = models.CharField(max_length=1000,default='圖片連結')    

class Price_001(models.Model):
    price_btn_001 = models.CharField(max_length=1000,default='',verbose_name = '選項名稱') 
    price_txt_001 = RichTextField(max_length=1000,default='輸入文字敘述',blank=True, null=True,verbose_name = '內容')

    def __str__(self):
        return "婚紗單拍內容" + str(self.id) + " 號 "  

    class Meta:
        verbose_name_plural = '婚紗單拍'
        verbose_name = '婚紗單拍'

class Price_002(models.Model):
    price_btn_002 = models.CharField(max_length=1000,default='按鈕名稱',verbose_name = '選項名稱') 
    price_txt_002 = RichTextField(max_length=1000,default='輸入文字敘述',blank=True, null=True,verbose_name = '內容')    

    def __str__(self):
        return "孕婦寫真內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '孕婦寫真'
        verbose_name = '孕婦寫真'       

class Price_003(models.Model):
    price_btn_003 = models.CharField(max_length=1000,default='按鈕名稱',verbose_name = '選項名稱') 
    price_txt_003 = RichTextField(max_length=1000,default='輸入文字敘述',blank=True, null=True,verbose_name = '內容')   

    def __str__(self):
        return "同性內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '同志寫真｜同性婚紗'
        verbose_name = '同志寫真｜同性婚紗'        

class Price_004(models.Model):
    price_btn_004 = models.CharField(max_length=1000,default='按鈕名稱',verbose_name = '選項名稱') 
    price_txt_004 = RichTextField(max_length=1000,default='輸入文字敘述',blank=True, null=True,verbose_name = '內容')     

    def __str__(self):
        return "婚紗包套內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '婚紗包套'
        verbose_name = '婚紗包套'        

class Pn_001(models.Model):
    pn_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結')

    def __str__(self):
        return "孕婦寫真內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '攝影作品-孕婦寫真'
        verbose_name = '攝影作品-孕婦寫真'     

class Pf_001(models.Model):
    pf_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結')

    def __str__(self):
        return "專業形象內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '攝影作品-專業形象照片'
        verbose_name = '攝影作品-專業形象照片'   

class Cp_001(models.Model):
    cp_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結')  

    def __str__(self):
        return "情侶寫真內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '攝影作品-情侶寫真'
        verbose_name = '攝影作品-情侶寫真'  

class Sg_001(models.Model):
    sg_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結')

    def __str__(self):
        return "單身婚紗內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '攝影作品-單身婚紗'
        verbose_name = '攝影作品-單身婚紗'  

class Pt_001(models.Model):
    pt_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結')

    def __str__(self):
        return "寵物婚紗內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '攝影作品-寵物婚紗'
        verbose_name = '攝影作品-寵物婚紗'  

class at_001(models.Model):
    at_tit_001 = models.CharField(max_length=1000,default='標題',verbose_name = '活動名稱')
    at_ph_001 = models.CharField(max_length=1000,default='活動圖照',verbose_name = '照片連結')
    at_con_001 = RichTextField(max_length=1000,default='活動內容',blank=True, null=True,verbose_name = '活動內容')

    def __str__(self):
        return "活動內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '活動專區'
        verbose_name = '活動專區'  

class Wedding_01(models.Model):
    Wedding_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結')

    def __str__(self):
        return "古裝內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '古裝婚紗'
        verbose_name = '古裝婚紗'  

class Wedding_02(models.Model):
    Wedding_02_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結')

    def __str__(self):
        return "景點內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '景點婚紗'
        verbose_name = '景點婚紗'  

class Wedding_03(models.Model):
    Wedding_03_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結')

    def __str__(self):
        return "摩登內容" + str(self.id) + " 號 " 

    class Meta:
        verbose_name_plural = '摩登婚紗'
        verbose_name = '摩登婚紗'  

class Wedding_04(models.Model):
    Wedding_04_ph_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結' ) 

    def __str__(self):
        return "韓系內容" + str(self.id) + " 號 "  

    class Meta:
        verbose_name_plural = '韓系婚紗'
        verbose_name = '韓系婚紗'  
          
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




