from django.contrib import admin
from .models import ProductCatalog, CatalogItem

class CatalogItemInline(admin.TabularInline):
    model = CatalogItem
    extra = 1  # Number of blank forms for adding items
    fields = ('title', 'description', 'icon')

@admin.register(ProductCatalog)
class ProductCatalogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CatalogItemInline]

@admin.register(CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_catalog')
    search_fields = ('title', 'description')
