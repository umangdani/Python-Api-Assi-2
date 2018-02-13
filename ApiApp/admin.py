from django.contrib import admin
from ApiApp.models import *

# Register your models here.


class DiscussionAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('Discussion data', {'fields': ('title', 'text', 'd_type','added_by', 'image')}),
	    ('Date', {'fields': ('created_date','modified_date',)}),
	    
	)

	
	search_fields = ('title',)
	ordering = ('-created_date',)
	list_display = ('title', 'd_type','added_by')
	list_display_links = ('title', 'd_type')
	

	def enable(self, request, queryset):
		queryset.update(is_active=True)



class CommentsAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('Comments data', {'fields': ('discussion', 'text','added_by')}),
	    ('Date', {'fields': ('created_date','modified_date',)}),
	    
	)

	search_fields = ('discussion',)
	ordering = ('-created_date',)
	list_display = ('discussion', 'text','added_by')
	list_display_links = ('discussion')
	

	def enable(self, request, queryset):
		queryset.update(is_active=True)



admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Comments,CommentsAdmin)

