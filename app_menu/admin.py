from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass
