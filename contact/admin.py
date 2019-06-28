from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from . models import Contact
class ContactsAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'gender', 'email', 'info', 'phone')
	list_editable = ('info',)
	list_per_page = 10
	search_field = ('name', 'gender', 'email', 'info', 'phone')
	list_filter = ('gender', 'date_added')
admin.site.register(Contact, ContactsAdmin)
admin.site.unregister(Group)