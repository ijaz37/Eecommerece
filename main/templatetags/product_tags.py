from django.contrib.auth.models import User

from django import template
from ..models import Cart, Product

register = template.Library()


@register.simple_tag()
def countproduct():
    return Cart.objects.filter(user_id=1).count()


@register.inclusion_tag("product.html")
def product(user):
    id=user.id
    myproduct = Cart.objects.filter(user=user.id)
    context = {
        'myproduct': myproduct,
        'id': id
    }
    return context
