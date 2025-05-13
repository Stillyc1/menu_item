from django.contrib import admin

from menu_item.models import MenuItem


@admin.register(MenuItem)
class UserMailAdmin(admin.ModelAdmin):
    """Отображение объекта модели MenuItem в админке."""

    list_display = ('title', 'parent')
    list_filter = ('title', 'parent')
    search_fields = ('title',)
