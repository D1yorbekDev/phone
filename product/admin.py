from django.contrib import admin
from .models import TypeProduct, Product
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'type', 'name', 'price', 'discount')
    list_display_links = ('id', 'type', 'name', 'price', 'discount')
    search_fields = ("name", )
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id', 'name')

@admin.register(TypeProduct)
class TypeProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    search_help_text = f'search in: {" or ".join(search_fields)}'
    ordering = ('id',)
