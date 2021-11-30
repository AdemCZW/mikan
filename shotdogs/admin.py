from django.contrib import admin
from .models import Shotdogs_photo, Home, Price
# Register your models here.
class Shotdogs_photoAdmin(admin.ModelAdmin):
	list_display = ()

admin.site.register(Shotdogs_photo)	

class Shotdogs_hmoeAdmin(admin.ModelAdmin):
	list_display = ()

admin.site.register(Home)	

class Shotdogs_priceAdmin(admin.ModelAdmin):
	list_display = ()

admin.site.register(Price)	

