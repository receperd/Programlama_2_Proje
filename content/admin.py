from django.contrib import admin

from content.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','status']
    list_filter=['status']

admin.site.register(Category,CategoryAdmin)