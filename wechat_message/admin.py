from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('keyword',)
    list_per_page = 12


admin.site.register(Message, MessageAdmin)
