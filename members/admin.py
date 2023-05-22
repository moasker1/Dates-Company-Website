from django.contrib import admin
from .models import Member
from .models import Product
from .models import Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','category']    
    search_fields = ['name', 'price', 'category']
    list_filter = ['category', 'price']
    


admin.site.register(Member)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)


admin.site.site_header = 'الطاقة الماسة للتمور (الإدارة)'
admin.site.site_title = "admin_panel"
