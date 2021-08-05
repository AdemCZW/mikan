from django.contrib import admin
from .models import Todo,Customer,Flight,Movie



class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','name', 'finish', 'created')


admin.site.register(Todo, TodoAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'tel')  # 顯示欄位
admin.site.register(Customer, CustomerAdmin)  # 加入至Administration(管理員後台)


class FlightAdmin(admin.ModelAdmin):
	list_display = ('user', 'items', 'fromname', 'pd_name', 'description', 'finish')
		
admin.site.register(Flight)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year')
 
admin.site.register(Movie, MovieAdmin)