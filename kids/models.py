from django.db import models
from ckeditor.fields import RichTextField

class kid_index(models.Model):
	kid_home_001 = models.CharField(max_length=1000,default='',verbose_name = '活動種類-1',blank=True)
	kid_home_002 = models.CharField(max_length=1000,default='',verbose_name = '活動標題-1',blank=True)
	kid_home_003 = models.CharField(max_length=1000,default='',verbose_name = '活動日期-1',blank=True)
	kid_home_004 = models.CharField(max_length=1000,default='',verbose_name = '活動連結-1',blank=True)
	kid_home_005 = models.CharField(max_length=1000,default='',verbose_name = '活動種類-2',blank=True)
	kid_home_006 = models.CharField(max_length=1000,default='',verbose_name = '活動標題-2',blank=True)
	kid_home_007 = models.CharField(max_length=1000,default='',verbose_name = '活動日期-2',blank=True)
	kid_home_008 = models.CharField(max_length=1000,default='',verbose_name = '活動連結-2',blank=True)
	kid_home_009 = models.CharField(max_length=1000,default='',verbose_name = '活動種類-3',blank=True)
	kid_home_010 = models.CharField(max_length=1000,default='',verbose_name = '活動標題-3',blank=True)
	kid_home_011 = models.CharField(max_length=1000,default='',verbose_name = '活動日期-3',blank=True)
	kid_home_012 = models.CharField(max_length=1000,default='',verbose_name = '活動連結-3',blank=True)

	kid_service_001 = models.CharField(max_length=1000,default='',verbose_name = '服務標題-1',blank=True)
	kid_service_002 = models.CharField(max_length=1000,default='',verbose_name = '服務內容-1',blank=True)
	kid_service_003 = models.CharField(max_length=1000,default='',verbose_name = '服務標題-2',blank=True)
	kid_service_004 = models.CharField(max_length=1000,default='',verbose_name = '服務內容-2',blank=True)
	kid_service_005 = models.CharField(max_length=1000,default='',verbose_name = '服務標題-3',blank=True)
	kid_service_006 = models.CharField(max_length=1000,default='',verbose_name = '服務內容-3',blank=True)
	kid_service_007 = models.CharField(max_length=1000,default='',verbose_name = '服務標題-4',blank=True)
	kid_service_008 = models.CharField(max_length=1000,default='',verbose_name = '服務內容-4',blank=True)

	kid_photos_001 = models.CharField(max_length=1000,default='',verbose_name = '情境',blank=True)
	kid_photos_002 = models.CharField(max_length=1000,default='',verbose_name = '抓周',blank=True)
	kid_photos_003 = models.CharField(max_length=1000,default='',verbose_name = '道具',blank=True)
	kid_photos_004 = models.CharField(max_length=1000,default='',verbose_name = '新生兒',blank=True)

	kid_plans_001 = models.CharField(max_length=1000,default='',verbose_name = 'Ａ方案-原價',blank=True)
	kid_plans_002 = models.CharField(max_length=1000,default='',verbose_name = 'Ａ方案-特價',blank=True)
	kid_plans_003 = RichTextField(max_length=2000,default='輸入',blank=True, null=True,verbose_name = 'Ａ方案-內容')
	kid_plans_004 = models.CharField(max_length=1000,default='',verbose_name = 'Ｂ方案-原價',blank=True)
	kid_plans_005 = models.CharField(max_length=1000,default='',verbose_name = 'Ｂ方案-特價',blank=True)
	kid_plans_006 = RichTextField(max_length=2000,default='輸入',blank=True, null=True,verbose_name = 'Ｂ方案-內容')
	kid_plans_007 = models.CharField(max_length=1000,default='',verbose_name = 'Ｃ方案-原價',blank=True)
	kid_plans_008 = models.CharField(max_length=1000,default='',verbose_name = 'Ｃ方案-特價',blank=True)
	kid_plans_009 = RichTextField(max_length=2000,default='輸入',blank=True, null=True,verbose_name = 'Ｃ方案-內容')

	kid_phone_001 = models.CharField(max_length=1000,default='',verbose_name = '電話',blank=True)
	kid_mail_001 = models.CharField(max_length=1000,default='',verbose_name = '信箱',blank=True)
	kid_line_001 = models.CharField(max_length=1000,default='',verbose_name = 'line',blank=True)
	kid_fb_001 = models.CharField(max_length=1000,default='',verbose_name = 'facebook',blank=True)
	kid_ig_001 = models.CharField(max_length=1000,default='',verbose_name = 'instagram',blank=True)
	
	def __str__(self):
		return "兒童抓周網站" + str(self.id) + " 號 " 

	class Meta:
		verbose_name_plural = '兒童抓周網站'
		verbose_name = '兒童抓周網站'
