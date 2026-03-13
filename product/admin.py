from django.contrib import admin
from .models import Category, Product, Review, UserConfirm

# Register your models here.
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(UserConfirm)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'created', 'updated')
    list_filter = ('category', )
