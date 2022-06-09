from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
	ordering = ('-id',)
	list_display_links = ('username', 'mobile')
	list_filter = [ 'is_active', 'is_staff', 'is_superuser']
	list_display = ['username', 'email', 'mobile', 'gender', 'first_name', 'last_name',]
	search_fields = ['username','email', 'mobile', 'gender', 'first_name', 'last_name']
	add_fieldsets = (
		(None, {
			'classes': ('wide', 'extrapretty'),
			'fields': ('first_name', 'last_name', 'email', 'mobile', 'username', 'password1', 'password2' ),
		}),
	)
	fieldsets = [
		(None, {'fields': ('email', 'username', 'mobile', 'first_name', 'last_name', 'password',)}),
		('Personal info', {'fields': ('phone', 'gender', 'dob', 'about' )}),
		('Permissions', {'classes': ('collapse', ), 'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
		('Important dates', {'classes': ('collapse', ), 'fields': ('last_login','date_joined')})]

class SkillAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	filter_fields = ('title', )

class TagAdmin(admin.ModelAdmin):
	list_display = ('title', 'status')
	filter_fields = ('title', )

class JobAdmin(admin.ModelAdmin):
	list_display = ('title', 'designation', 'max_experiance', 'author', 'status')
	filter_fields = ('title', 'designation', 'author')

class ApplicantAdmin(admin.ModelAdmin):
	list_display = ('fname', 'designation', 'experiance', 'status')
	filter_fields = ('fname', 'designation')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Applicant, ApplicantAdmin)