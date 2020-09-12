from django.contrib import admin
from category_management.models import Category,Subcategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','type']
    list_search  = ['name']

admin.site.register(Category,CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category']
    list_search  = ['name','category']

admin.site.register(Subcategory,SubCategoryAdmin)