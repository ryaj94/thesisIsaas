from django.contrib import admin

# Register your models here.

from .models import *

admin.site.site_header = "Isaas Admin"
admin.site.site_title = "Isaas Admin Area"
admin.site.index_title = "Welcome to the Isaas Admin Area"

class UserAdmin(admin.ModelAdmin):
    list_display = ('user','user_fname','user_mname','user_lname','user_course','user_yrandsec','user_address','user_cnumber')
    search_fields = ['user__username','user_yrandsec','user_lname']

class UserGrade(admin.ModelAdmin):
    search_fields = ['user__username']

admin.site.register(studentprof, UserAdmin )
admin.site.register(studentgrades, UserGrade)
admin.site.register(fy2ndsem, UserGrade)
admin.site.register(sy1stsem, UserGrade)
admin.site.register(sy2ndsem, UserGrade)
admin.site.register(sysummer, UserGrade)
admin.site.register(ty1stsem, UserGrade)
admin.site.register(ty2ndsem, UserGrade)
admin.site.register(fy1stsem, UserGrade)
admin.site.register(fry2ndsem, UserGrade)
admin.site.register(adviserprof)
