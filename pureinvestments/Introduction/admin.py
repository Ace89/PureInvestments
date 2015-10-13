from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
	(None,			{'fields': ['message_name']}),
	(None,			{'fields': ['message_contact']}),
	(None,			{'fields': ['message_body']}),
	('Date information',	{'fields': ['pub_date']}),
]
    
    list_display = ('message_name','message_contact','message_body','pub_date','was_published_recently')
    list_filetr = ['pub_date']
    search_fields = ['message_name']


admin.site.register(Message, MessageAdmin)
