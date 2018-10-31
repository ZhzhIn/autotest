from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['productname']}),
        ('Date information',{'fields':['create_time'],'classes':['collapse']}),
    ]
    list_display=['id','productname','productdesc','producter','create_time']
    list_filter=['create_time','producter']
    search_fields=['productname','producter']
admin.site.register(Product,ProductAdmin)