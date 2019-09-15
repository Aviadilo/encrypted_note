from django.contrib import admin

from .models import Note, Category


class NoteAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category']


admin.site.register(Note, NoteAdmin)
admin.site.register(Category)
