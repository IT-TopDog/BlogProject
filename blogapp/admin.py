from django.contrib import admin
from .models import Author, Categoty, Article
from django.utils.safestring import mark_safe


class AdminAuthor(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'date',)
    list_display_links = ('first_name',)

class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

class AdminArticle(admin.ModelAdmin):
    list_display = ('id', 'heading', 'author', 'category', 'publication_date',)
    list_display_links = ('author','heading',)
    list_filter = ('author', 'category',)

admin.site.register(Author, AdminAuthor)
admin.site.register(Categoty, AdminCategory)
admin.site.register(Article, AdminArticle)

# Register your models here.
