from django.contrib import admin
from .models import CatalogSection, CatalogItem

@admin.register(CatalogSection)
class CatalogSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'section')
    search_fields = ('title',)
    list_filter = ('section',)
