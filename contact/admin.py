from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Contact
from import_export.admin import ImportExportModelAdmin
class ContactsAdmin(ImportExportModelAdmin):
	list_display = ('id','name', 'gender', 'email', 'info', 'phone')
	list_display_links = ('id', 'name')
	list_editable = ('info',)
	list_per_page = 10
	search_field = ('name', 'gender', 'email', 'info', 'phone')
	list_filter = ('gender', 'date_added')
admin.site.register(Contact, ContactsAdmin)
admin.site.unregister(Group)