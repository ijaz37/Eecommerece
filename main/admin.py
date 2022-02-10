from django.contrib import admin
from .models import Cart, Category, Company,Contact, Product, Product_Detail, Images, Product_Description,ShippingAddress,ShopingHistory, Additional_Information, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'discount', 'image', 'is_trending', 'category')


@admin.register(Product_Detail)
class Product_detail(admin.ModelAdmin):
    list_display = ('title', 'image', 'discount', 'category', 'available', 'info', 'warranty',)


@admin.register(Images)
class Images(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Product_Description)
class Product_detail_description(admin.ModelAdmin):
    list_display = ('product_heading_one', 'product_image_one', 'product_description_one')


@admin.register(Additional_Information)
class Aditional_information(admin.ModelAdmin):
    list_display = ('heading', 'description')


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('title', 'name',)


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'single_total')


@admin.register(ShippingAddress)
class Shippingaddress(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'company_name', 'area_code', 'primary_phone','street_address1', 'street_address2', 'zip_code', 'business_address',)


@admin.register(ShopingHistory)
class ShopingHistory(admin.ModelAdmin):
    list_display = ('user', 'is_order', 'total',)


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message',)