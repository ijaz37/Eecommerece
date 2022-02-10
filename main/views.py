import json

from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView
from .models import Product, Company, Category, Cart, Product_Detail, Review, Images, Product_Description, \
    Additional_Information, ShippingAddress, ShopingHistory
from .forms import ReviewForm, ShippingForm, PaymentForm, ContactForm
import stripe
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'

from django.http import JsonResponse


# class Home(ListView):
#     model = Product
#     template_name = 'main/index.html'

def home(request):
    trending = Product.objects.filter(is_trending=True)[:6]
    mobile = Product.objects.filter(category__name='Mobile')[:6]
    tablet = Product.objects.filter(category__name='Tablet')[:6]
    Mobile_company = Company.objects.filter(category__name='Mobile')
    Tablet_company = Company.objects.filter(category__name='Tablet')

    context = {
        'trending': trending,
        'mobile': mobile,
        'tablet': tablet,
        'mobile_company': Mobile_company,
        'tablet_company': Tablet_company
    }
    return render(request, 'main/index.html', context)


class HomeFixed(TemplateView):
    template_name = 'main/index_fixed_header.html'


class HomeInverse(TemplateView):
    template_name = 'main/index_inverse_header.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'name': 'ijaz'
        }
        return context


def getallproduct(request, pk):
    product = Product.objects.filter(category__name='Mobile', company__id=pk)
    print(product)

    context = {
        'mobile': product
    }
    return render(request, 'main/formMobile.html', context)


def gettablet(request, pk):
    print("tab")
    tablet = Product.objects.filter(category__name='Tablet', company__id=pk)
    context = {
        'tablet': tablet,
    }
    return render(request, 'main/tabletproduct.html', context)


def product_detail(request, pk):
    form = ReviewForm()
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        form = ReviewForm(request.POST)
        forms = form.save(commit=False)
        forms.product = product
        if form.is_valid():
            forms.save()
    detail = Product_Detail.objects.filter(id=pk)
    images = Images.objects.filter(product_id=pk)
    description = Product_Description.objects.get(id=pk)
    information = Additional_Information.objects.filter(product_id=pk)
    review = Review.objects.filter(product_id=pk)
    product = Product.objects.filter(id=pk)
    count = Review.objects.filter(product_id=pk).count()
    product = Product.objects.all()[:6]
    product_id = Product.objects.only('id')

    context = {
        'detail': detail,
        'images': images,
        'description': description,
        'information': information,
        'product': product,
        'review': review,
        'form': form,
        'count': count,
        'product_id': product_id
    }
    print(product_id)
    return render(request, 'main/product_detail.html', context)


def add_to_cart(request, pk):
    user = request.user
    # product = request.GET.get('product_id')
    cart = Cart(user=user, product_id=pk)

    if Cart.objects.filter(user=user, product_id=pk).exists():
        item = Cart.objects.get(product_id=pk, user=request.user)
        item.quantity += 1

    else:
        cart.save()

    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shiping = 0.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                signle_total = (p.quantity * p.product.price)
                amount = amount + float(signle_total)
                if p.product_id == pk:
                    item = Cart.objects.get(product_id=p.product_id, user=request.user)
                    signle_total = (p.quantity * p.product.price)
                    item.single_total = signle_total
                    item.save()
                total_amount = amount + shiping
            context = {
                'cart': cart,
                'signle_total': signle_total,
                'amount': amount,
                'total_amount': total_amount,
                'id': pk
            }
        return render(request, 'main/checkout/checkout_cart.html', context)


#
# def review(request):
#
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form = ReviewForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'main/product_detail.html', context)
# # class Product(ListView):
#     template_name = 'main/product.html'


class Contact(TemplateView):
    template_name = 'main/contact_us.html'


# class ProductDetail(TemplateView):
#   template_name = 'main/product_detail.html'


def inceament(request, pk):
    print(pk)
    c = Cart.objects.get(Q(product_id=pk) & Q(user=request.user))
    c.quantity += 1
    c.save()
    amount = 0.0
    shiping = 0.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
        signle_total = (p.quantity * p.product.price)
        amount = amount + float(signle_total)
        total_amount = amount + shiping

    context = {
        'quantity': c.quantity,
        'amount': amount,
        'single_total': signle_total,
        'total_amount': total_amount
    }
    return render(request, 'main/checkout/checkout_cart.html', context)


def deceament(request, pk):
    c = Cart.objects.get(Q(product_id=pk) & Q(user=request.user))
    c.quantity -= 1
    c.save()
    amount = 0.0
    shiping = 0.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
        signle_total = (p.quantity * p.product.price)
        amount = amount + float(signle_total)
        total_amount = amount + shiping

    context = {
        'quantity': c.quantity,
        'amount': amount,
        'single_total': signle_total,
        'total_amount': total_amount
    }
    return render(request, 'main/checkout/checkout_cart.html', context)


def checkout_info(request):
    username = request.user.username
    email = request.user.email
    customer = stripe.Customer.create(
        description=username,
        email=email
    )

    form = ShippingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Successfully submitted")

        else:
            print("invalid form")
            messages.success(request, "invalid form")

    context = {
        'form': form,
    }
    return render(request, 'main/checkout/checkout_info.html', context)


def checkout_payment(request):
    form = PaymentForm()
    context = {
        'form': form
    }
    return render(request, 'main/checkout/checkout_payment.html', context)


@csrf_exempt
def checkout_session(request):
    amount = 0.0
    shiping = 0.0
    total_amount = 0.0
    pro = []
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    print(cart_product)
    shoping = ShopingHistory(user=request.user, is_order=True)

    shoping.save()
    for p in cart_product:
        shoping.items.add(p.product)
        pitem = Product.objects.get(id=p.product_id)
        pro.append(pitem)
        signle_total = (p.quantity * p.product.price)
        amount = amount + float(signle_total)
        total_amount = amount + shiping
    shoping.total=total_amount
    shoping.save()
    cart=Cart.objects.filter(user=request.user)
    cart.delete()
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # product=Product.objects.get(id=pid)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():

            token = stripe.Token.create(
                card={
                    "name": form.cleaned_data['cardholder_name'],
                    "number": form.cleaned_data['card_number'],
                    "exp_month": form.cleaned_data['expired_month'],
                    "exp_year": form.cleaned_data['expired_year'],
                    "cvc": form.cleaned_data['csc'],
                },
            )
            # customer = stripe.Customer.create_source(
            #     "cus_L75oV9YPdHn3QR",
            #     source=request.user.id,
            # )

            charge = stripe.Charge.create(
                amount=int(total_amount*100),
                currency="usd",
                source=token,# obtained above
                # source="tok_visa", # obtained with Stripe.js (JS)
                description="Charge for jenny.rosen@example.com"
            )


    context = {
        'sub_total': amount,
        'total': total_amount,
        'cart_product': cart_product,
        'pro': pro
    }
    return render(request, 'main/checkout/checkout_complete.html', context)


            # charge = stripe.Charge.create(
            #     amount=2000,
            #     currency="usd",
            #     source=token.id,  # obtained above
            #     # source="tok_visa", # obtained with Stripe.js (JS)
            #     description="Charge for jenny.rosen@example.com"
            # )
    # session = stripe.checkout.Session.create(
    #     payment_method_types=['card'],
    #     line_items=[
    #         {
    #             'price_data': {
    #                 'currency': 'usd',
    #                 'product_data': {
    #                     'name': "samsung",
    #                 },
    #                 'unit_amount': 87,
    #             },
    #             'quantity': 1,
    #         }],
    #     mode='payment',
    #     success_url="http://127.0.0.1:8000/payment_success",
    #     cancel_url="http://127.0.0.1:8000/payment_cancel",

    # )
    # return redirect(session.url, 303)


def contact_us(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact_us.html', context)