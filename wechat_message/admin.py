from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'created', 'updated')

admin.site.register(Message, MessageAdmin)
