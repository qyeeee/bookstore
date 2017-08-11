from django.contrib import admin
from store_users.models import *

class STUserAdmin(admin.ModelAdmin):
    list_display = ['id','name','user', 'phone', 'got_books', 'card_id']


admin.site.register(STUser,STUserAdmin)
