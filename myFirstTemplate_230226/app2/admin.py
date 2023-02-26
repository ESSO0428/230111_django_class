"""
from django.contrib import admin

# Register your models here.
"""

from django.contrib import admin
from .models        import Post, Product
#from Post          import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pumps', 'pub_date')


admin.site.register(Post   , PostAdmin)
admin.site.register(Product, ProductAdmin)

