from django.contrib import admin

from content.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','status','image_tag']
    list_filter=['status','image']

admin.site.register(Category,CategoryAdmin)