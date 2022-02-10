from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    stripe_customer_id = models.CharField(max_length=120)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Company(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    discount = models.IntegerField()
    is_trending = models.BooleanField(default=False)
    old_price = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.image.url


class Product_Detail(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=False, blank=False)
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    available = models.BooleanField(default=False)
    warranty = models.IntegerField(null=True, blank=True)
    info = models.TextField(max_length=500, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_price')

    def __str__(self):
        return self.title


class Product_Description(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    product_heading_one = models.CharField(max_length=40)
    product_image_one = models.ImageField(null=False, blank=False)
    product_description_one = models.TextField(max_length=700)

    product_heading_two = models.CharField(max_length=40)
    product_image_two = models.ImageField(null=False, blank=False)
    product_description_two = models.TextField(max_length=700)

    product_heading_three = models.CharField(max_length=40)
    product_image_three = models.ImageField(null=False, blank=False)
    product_description_three = models.TextField(max_length=700)

    product_heading_four = models.CharField(max_length=40)
    product_image_four = models.ImageField(null=False, blank=False)
    product_description_four = models.TextField(max_length=700)

    product_heading_five = models.CharField(max_length=40)
    product_image_five = models.ImageField(null=False, blank=False)
    product_description_five = models.TextField(max_length=700)


class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    heading = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return self.heading


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    name = models.CharField(max_length=30)
    review = models.TextField(max_length=1000)
    rating = models.CharField(max_length=5)
    ondate = models.DateTimeField(datetime, default=datetime.now())


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    single_total = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    area_code = models.IntegerField()
    primary_phone = models.IntegerField()
    street_address1 = models.CharField(max_length=100)
    street_address2 = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    business_address = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class Payment(models.Model):
    cardholder_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=1999)
    expired_month = models.CharField(max_length=2, default="MM")
    expired_year = models.CharField(max_length=2, default="YY")
    csc = models.CharField(max_length=200)

    def __str__(self):
        return self.cardholder_name


class ShopingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    is_order = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name