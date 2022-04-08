from django.contrib import admin
from .models import Customer,Flight,Index_001, Price_002,Studio_001,Service_001,Price_001, Price_002, Price_003, Price_004, Pn_001, Pf_001, Cp_001, Sg_001, Pt_001, at_001, Wedding_01, Wedding_02, Wedding_03, Wedding_04



class IndexAdmin(admin.ModelAdmin):
	list_display = ('mid_001','mid_002','mid_003','mid_004','mid_005','mid_006',
					'mid_txt_001','mid_txt_002','mid_txt_003','mid_txt_004','mid_txt_005','mid_txt_006'
		)
admin.site.register(Index_001)

class StudioAdmin(admin.ModelAdmin):
	list_display = ('studio_ph_001',)

admin.site.register(Studio_001)	

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('service_ph_001',)

admin.site.register(Service_001)	

class Price001Admin(admin.ModelAdmin):
	list_display = ('price_btn_001','price_txt_001')

admin.site.register(Price_001)	

class Price002Admin(admin.ModelAdmin):
	list_display = ('price_btn_002','price_txt_002')

admin.site.register(Price_002)	

class Price003Admin(admin.ModelAdmin):
	list_display = ('price_btn_003','price_txt_003')

admin.site.register(Price_003)	

class Price004Admin(admin.ModelAdmin):
	list_display = ('price_btn_004','price_txt_004')

admin.site.register(Price_004)	

class Pn001Admin(admin.ModelAdmin):
	list_display = ('pn_ph_001')

admin.site.register(Pn_001)	

class Pf001Admin(admin.ModelAdmin):
	list_display = ('pf_ph_001')

admin.site.register(Pf_001)	

class Cp001Admin(admin.ModelAdmin):
	list_display = ('cp_ph_001')

admin.site.register(Cp_001)	

class Sg001Admin(admin.ModelAdmin):
	list_display = ('sg_ph_001')

admin.site.register(Sg_001)	

class Pt001Admin(admin.ModelAdmin):
	list_display = ('pt_ph_001')

admin.site.register(Pt_001)	

class at001Admin(admin.ModelAdmin):
	list_display = ('at_tit_001','at_con_001','at_ph_001')

admin.site.register(at_001)	

class Wedding001Admin(admin.ModelAdmin):
	list_display = ('Wedding_ph_001')

admin.site.register(Wedding_01)	

class Wedding002Admin(admin.ModelAdmin):
	list_display = ('Wedding_02_ph_001')

admin.site.register(Wedding_02)	

class Wedding003Admin(admin.ModelAdmin):
	list_display = ('Wedding_03_ph_001')

admin.site.register(Wedding_03)	

class Wedding004Admin(admin.ModelAdmin):
	list_display = ('Wedding_04_ph_001')

admin.site.register(Wedding_04)	





