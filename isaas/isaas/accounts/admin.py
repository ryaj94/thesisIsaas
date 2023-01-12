from django.contrib import admin

# Register your models here.

from .models import *

admin.site.site_header = "Isaas Admin"
admin.site.site_title = "Isaas Admin Area"
admin.site.index_title = "Welcome to the Isaas Admin Area"

class UserAdmin(admin.ModelAdmin):
    list_display = ['user','user_fname','user_mname','user_lname','user_course','user_yrandsec','user_address','user_cnumber']
    search_fields = ['user_id','user_fname','user_mname','user_lname','user_course','user_yrandsec','user_address','user_cnumber']


admin.site.register(studentprof, UserAdmin )
admin.site.register(studentgrades)
admin.site.register(fy2ndsem)
admin.site.register(sy1stsem)
admin.site.register(sy2ndsem)
admin.site.register(sysummer)
admin.site.register(ty1stsem)
admin.site.register(ty2ndsem)
admin.site.register(fy1stsem)
admin.site.register(fry2ndsem)
admin.site.register(adviserprof)
