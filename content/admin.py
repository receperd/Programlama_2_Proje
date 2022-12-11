from django.contrib import admin

from content.models import Category, Content, Images


# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','status']
    list_filter=['status']

class ContentAdmin(admin.ModelAdmin):
    list_display=['title','category','image_tag','status']
    readonly_fields = ('image_tag',)
    list_filter=['status','category']
    inlines = [ProductImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display=['title','content','image']


admin.site.register(Category,CategoryAdmin) #categorynin admin panelinde gösterilmesi
admin.site.register(Content,ContentAdmin) #contentin admin panelinde gösterilmesi
admin.site.register(Images,ImagesAdmin) #imagesin admin panelinde gösterilmesi