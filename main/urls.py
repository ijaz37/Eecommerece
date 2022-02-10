from django.urls import path
from .views import add_to_cart, contact_us, checkout_info, checkout_payment,checkout_session, getallproduct, gettablet, home,inceament, deceament, HomeFixed, HomeInverse, Product, product_detail

urlpatterns = [
    path('', home, name='home'),

    path('contact/', contact_us, name='contact'),
    path('homefix/', HomeFixed.as_view(), name='homefix'),
    path('homeinverse/', HomeInverse.as_view(), name='homeinverse'),
    # path('product', Product.as_view(), name='product'),

    # path('getallproduct/', getallproduct, name= 'getallproduct'),
    path('getallproduct/<int:pk>', getallproduct, name='getallproduct'),
    path('gettablet/<int:pk>', gettablet, name='gettablet'),
    path('product-detail/<int:pk>', product_detail, name='product-detail'),
    # path('review/', review, name='review')

    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),

    path('increment/<int:pk>', inceament, name='increment'),
    path('decrement/<int:pk>', deceament, name='decrement'),

    path('checkout_info/', checkout_info, name='checkout_info'),
    path('checkout_payment/', checkout_payment, name='checkout_payment'),
    path('checkout_session/', checkout_session, name='checkout_session'),


]
