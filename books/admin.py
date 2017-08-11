from django.contrib import admin
from books.models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'photo']

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','got_authors', 'desc', 'photo', 'cost','download']



admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)


