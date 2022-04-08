from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class vh_index_001(models.Model):
	vh_banner_001 = models.CharField(max_length=1000,null=True,verbose_name = '置頂大圖',blank=True)
	vh_top_001 = models.CharField(max_length=1000,null=True,verbose_name = '左',blank=True)
	vh_top_002 = models.CharField(max_length=1000,null=True,verbose_name = '右上',blank=True)
	vh_top_003 = models.CharField(max_length=1000,null=True,verbose_name = '右下',blank=True)
	vh_mid_001 = models.CharField(max_length=1000,verbose_name = '標題名稱',blank=True)
	vh_mid_ph_001 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結',blank=True)
	vh_mid_txt_001 = models.TextField(max_length=1000,verbose_name = '內容',blank=True)
	vh_mid_002 = models.CharField(max_length=1000,verbose_name = '標題名稱',blank=True)
	vh_mid_ph_002 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結',blank=True)
	vh_mid_txt_002 = models.TextField(max_length=1000,verbose_name = '內容',blank=True)
	vh_mid_003 = models.CharField(max_length=1000,verbose_name = '標題名稱',blank=True)
	vh_mid_ph_003 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結',blank=True)
	vh_mid_txt_003 = models.TextField(max_length=1000,verbose_name = '內容',blank=True)
	vh_mid_004 = models.CharField(max_length=1000,verbose_name = '標題名稱',blank=True)
	vh_mid_txt_004 = models.TextField(max_length=1000,verbose_name = '內容',blank=True)
	vh_mid_ph_004 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結',blank=True)
	vh_mid_005 = models.CharField(max_length=1000,verbose_name = '標題名稱',blank=True)
	vh_mid_txt_005 = models.TextField(max_length=1000,verbose_name = '內容',blank=True)
	vh_mid_ph_005 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結',blank=True)
	vh_mid_006 = models.CharField(max_length=1000,verbose_name = '標題名稱',blank=True)
	vh_mid_txt_006 = models.TextField(max_length=1000,verbose_name = '內容',blank=True)
	vh_mid_ph_006 = models.CharField(max_length=1000,null=True,verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-首頁編輯"

	class Meta:
		verbose_name_plural = '手工-首頁'
		verbose_name = '手工-首頁'

class vh_studio_001(models.Model):
	vh_studio_001 = models.CharField(max_length=1000,default='',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-攝影棚照片連結" + str(self.id) + " 號 " 

	class Meta:
		verbose_name_plural = '手工-攝影棚圖片'
		verbose_name = '手工-攝影棚圖片'

class vh_style_001(models.Model):
	vh_style_st_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-自然景致照片連結" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = '手工-自然景致'
		verbose_name = '手工-自然景致'

class vh_style_002(models.Model):
	vh_style_st_002 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-幸福街角照片連結" + str(self.id) + " 號 " 

	class Meta:
		verbose_name_plural = '手工-幸福街角'
		verbose_name = '手工-幸福街角'    

class vh_style_003(models.Model):
	vh_style_st_003 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-風格內景照片連結" + str(self.id) + " 號 " 

	class Meta:
		verbose_name_plural = '手工-風格內景'
		verbose_name = '手工-風格內景'        

class vh_style_004(models.Model):
	vh_style_st_004 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-唯美光芒照片連結" + str(self.id) + " 號 "  

	class Meta:
		verbose_name_plural = '手工-唯美光芒'
		verbose_name = '手工-唯美光芒'

class vh_style_005(models.Model):
	vh_style_st_005 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-甜膩俏皮照片連結" + str(self.id) + " 號 " 

	class Meta:
		verbose_name_plural = '手工-甜膩俏皮'
		verbose_name = '手工-甜膩俏皮'

class vh_style_006(models.Model):
	vh_style_st_006 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-意境劇情照片連結" + str(self.id) + " 號 " 

	class Meta:
		verbose_name_plural = '手工-意境劇情'
		verbose_name = '手工-意境劇情'        

class vh_big_single(models.Model):
	vh_big_single_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-個人寫真照片連結" + str(self.id) + " 號 " 

	class Meta:
		verbose_name_plural = '手工-個人寫真'
		verbose_name = '手工-個人寫真'      

class vh_big_cpl(models.Model):
	vh_big_cpl_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-情侶寫真照片連結" + str(self.id) + " 號 " 

	class Meta:
		verbose_name_plural = '手工-情侶寫真'
		verbose_name = '手工-情侶寫真'    

class vh_big_frds(models.Model):
	vh_big_frds_001 = models.CharField(max_length=1000,default='圖片連結',verbose_name = '照片連結',blank=True)

	def __str__(self):
		return "手工-閨密寫真照片連結" + str(self.id) + " 號 "

	class Meta:
		verbose_name_plural = '手工-閨蜜寫真'
		verbose_name = '手工-閨蜜寫真'

