from django.contrib import admin

from core.models import Author, Book, Genre


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','gender','country_of_birth','date_of_birth')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('gender','date_of_birth')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_display_links = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','pages','genre','year_published','status')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('author','genre','year_published','status')