from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class Shotdogs_photo(models.Model):
    Photo_1001 = models.CharField(max_length=1000,verbose_name = '-狗狗-', blank=True ) 
    Photo_1002 = models.CharField(max_length=1000,verbose_name = '2', blank=True )
    Photo_1003 = models.CharField(max_length=1000,verbose_name = '3', blank=True )
    Photo_1004 = models.CharField(max_length=1000,verbose_name = '4', blank=True ) 
    Photo_1005 = models.CharField(max_length=1000,verbose_name = '5', blank=True )
    Photo_1006 = models.CharField(max_length=1000,verbose_name = '6', blank=True )
    Photo_1007 = models.CharField(max_length=1000,verbose_name = '7', blank=True )
    Photo_1008 = models.CharField(max_length=1000,verbose_name = '8', blank=True )
    Photo_1009 = models.CharField(max_length=1000,verbose_name = '9', blank=True )
    Photo_1010 = models.CharField(max_length=1000,verbose_name = '10', blank=True )

    Photo_2001 = models.CharField(max_length=1000,verbose_name = '-貓咪-', blank=True ) 
    Photo_2002 = models.CharField(max_length=1000,verbose_name = '2', blank=True )
    Photo_2003 = models.CharField(max_length=1000,verbose_name = '3', blank=True )
    Photo_2004 = models.CharField(max_length=1000,verbose_name = '4', blank=True ) 
    Photo_2005 = models.CharField(max_length=1000,verbose_name = '5', blank=True )
    Photo_2006 = models.CharField(max_length=1000,verbose_name = '6', blank=True )
    Photo_2007 = models.CharField(max_length=1000,verbose_name = '7', blank=True )
    Photo_2008 = models.CharField(max_length=1000,verbose_name = '8', blank=True )
    Photo_2009 = models.CharField(max_length=1000,verbose_name = '9', blank=True )
    Photo_2010 = models.CharField(max_length=1000,verbose_name = '10', blank=True )

    Photo_3001 = models.CharField(max_length=1000,verbose_name = '-婚紗-', blank=True ) 
    Photo_3002 = models.CharField(max_length=1000,verbose_name = '2', blank=True )
    Photo_3003 = models.CharField(max_length=1000,verbose_name = '3', blank=True )
    Photo_3004 = models.CharField(max_length=1000,verbose_name = '4', blank=True ) 
    Photo_3005 = models.CharField(max_length=1000,verbose_name = '5', blank=True )
    Photo_3006 = models.CharField(max_length=1000,verbose_name = '6', blank=True )
    Photo_3007 = models.CharField(max_length=1000,verbose_name = '7', blank=True )
    Photo_3008 = models.CharField(max_length=1000,verbose_name = '8', blank=True )
    Photo_3009 = models.CharField(max_length=1000,verbose_name = '9', blank=True )
    Photo_3010 = models.CharField(max_length=1000,verbose_name = '10', blank=True )

    Photo_4001 = models.CharField(max_length=1000,verbose_name = '-其他-', blank=True ) 
    Photo_4002 = models.CharField(max_length=1000,verbose_name = '2', blank=True )
    Photo_4003 = models.CharField(max_length=1000,verbose_name = '3', blank=True )
    Photo_4004 = models.CharField(max_length=1000,verbose_name = '4', blank=True ) 
    Photo_4005 = models.CharField(max_length=1000,verbose_name = '5', blank=True )
    Photo_4006 = models.CharField(max_length=1000,verbose_name = '6', blank=True )
    Photo_4007 = models.CharField(max_length=1000,verbose_name = '7', blank=True )
    Photo_4008 = models.CharField(max_length=1000,verbose_name = '8', blank=True )
    Photo_4009 = models.CharField(max_length=1000,verbose_name = '9', blank=True )
    Photo_4010 = models.CharField(max_length=1000,verbose_name = '10', blank=True )

    def __str__(self):
        return "攝狗狗-相簿照" + str(self.id) + " 號 "  

    class Meta:
        verbose_name_plural = '寵物寫真'
        verbose_name = '寵物寫真'  

class Home(models.Model):
	mid_ph_001 = models.CharField(max_length=1000,verbose_name = '輪播1', blank=True )
	mid_ph_002 = models.CharField(max_length=1000,verbose_name = '輪播2', blank=True )
	mid_ph_003 = models.CharField(max_length=1000,verbose_name = '輪播3', blank=True )

	def __str__(self):
		return "攝狗狗-首頁"

	class Meta:
		verbose_name_plural = "攝狗狗-首頁"
		verbose_name = "攝狗狗-首頁"

class Price(models.Model):
	Price_ph_001 = models.CharField(max_length=1000,verbose_name = '標題照片', blank=True )
	Price_txt_001 = models.CharField(max_length=1000,verbose_name = '標題', blank=True )
	Price_con_001 = RichTextField(max_length=2000,default='輸入',blank=True, null=True,verbose_name = '內容')

	def __str__(self):
		return "攝狗狗-套裝" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = "攝狗狗-套裝"
		verbose_name = "攝狗狗-套裝"

class article(models.Model):
    atc_tit_001 = models.CharField(max_length=1000,verbose_name = '文章標題', blank=True )
    atc_ph_001 = models.CharField(max_length=1000,verbose_name = '文張照片', blank=True )
    atc_con_001 = RichTextField(max_length=10000,default='輸入',blank=True, null=True,verbose_name = '內容')

    def __str__(self):
        return "攝狗狗-文章專區" + str(self.id) + " 號 "

    class Meta:
        verbose_name_plural = "攝狗狗-文章"
        verbose_name = "攝狗狗-文章"
        




