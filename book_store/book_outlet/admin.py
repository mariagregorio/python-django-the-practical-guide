from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating', 'is_bestselling')
    list_display = ('title', 'author', 'rating')

admin.site.register(Book, BookAdmin)
