from django.contrib import admin

from .models import News, Category


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'is_publishes')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_publishes',)
    list_filter = ('is_publishes',  'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)