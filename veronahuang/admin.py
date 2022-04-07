from django.contrib import admin
from .models import vh_index_001,vh_studio_001,vh_style_001,vh_style_002,vh_style_003,vh_style_004,vh_style_005,vh_style_006,vh_big_single,vh_big_cpl,vh_big_frds

class vh_index_001Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_index_001)	


class vh_studio_001Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_studio_001)	

class vh_style_001Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_style_001)	

class vh_style_002Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_style_002)	

class vh_style_003Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_style_003)	

class vh_style_004Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_style_004)	

class vh_style_005Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_style_005)	

class vh_style_006Admin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_style_006)	

class vh_big_singleAdmin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_big_single)	

class vh_big_cplAdmin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_big_cpl)	

class vh_big_frdsAdmin(admin.ModelAdmin):
	list_display = ()

admin.site.register(vh_big_frds)	
