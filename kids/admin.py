from django.contrib import admin
from .models import kid_index

class kid_01_Admin(admin.ModelAdmin):
	
	fieldsets = (
		['輪播', {
            'fields': ('kid_home_001', 'kid_home_002','kid_home_003', 'kid_home_004','kid_home_005', 'kid_home_006','kid_home_007', 'kid_home_008','kid_home_009', 'kid_home_010','kid_home_011', 'kid_home_012'),
        }],
        ['服務', {
            'fields': ('kid_service_001', 'kid_service_002','kid_service_003', 'kid_service_004','kid_service_005', 'kid_service_006','kid_service_007', 'kid_service_008'),
        }],
        ['種類', {
            'fields': ('kid_photos_001', 'kid_photos_002','kid_photos_003', 'kid_photos_004'),
        }],
        ['方案', {
            'fields': ('kid_plans_001', 'kid_plans_002','kid_plans_003', 'kid_plans_004','kid_plans_005', 'kid_plans_006','kid_plans_007', 'kid_plans_008','kid_plans_009'),
        }],
        ['聯繫資訊', {
            'fields': ('kid_phone_001', 'kid_mail_001','kid_line_001', 'kid_fb_001','kid_ig_001'),
        }],
    )

admin.site.register(kid_index, kid_01_Admin)	


# Register your models here.
