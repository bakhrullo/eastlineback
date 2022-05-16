from django.contrib import admin
from . import models


# Register your models here.
# class VoiceAdmin(admin.ModelAdmin):
#     list_display = ['userId', 'inVoiceId', 'price', 'cashBack', 'cashBackDate', 'inVoiceDate', 'name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['tgUserId', 'cashBack', 'phone', 'inVoiceId', 'price', 'cashBackDate', 'name']
    list_filter = ['phone']
    search_fields = ['phone', 'cashBack']


admin.site.register(models.UserInfo, UserAdmin)
# admin.site.register(models.Voice, VoiceAdmin)
