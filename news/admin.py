from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'is_publishes', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_publishes',)
    list_filter = ('is_publishes',  'category')
    filds = ('title', 'category', 'content', 'photo', 'get_photo', 'is_publishes', 'views',  'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views',  'created_at', 'updated_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return  'Фото не установлено'

    get_photo.short_description = 'Миниатюра'

    save_on_top = True

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'