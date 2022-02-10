from django import forms
from .models import Review, Product, ShippingAddress, Payment, Contact


class ReviewForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id': 'name'
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'email'
    }))
    review = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'review'
    }))

    rating = forms.CharField(widget=forms.TextInput(attrs={
        'type':'hidden',
        'class': 'radio-star-total',
        'id': 'total'
    }))

    class Meta:
        model = Review
        fields = ['name', 'title', 'review', 'rating']


class ShippingForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'first_name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'last_name'
    }))
    company_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'company_name'
    }))
    area_code = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'area_code'
    }))
    primary_phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'primary_phone'
    }))
    street_address1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control m-b-10',
        'name': 'street_address'
    }))
    street_address2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'street_address2'
    }))
    zip_code = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'zip_code'
    }))
    business_address = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'm-l-5 text-muted',
        'name': 'business_address'
    }))

    class Meta:
        model = ShippingAddress
        fields = ['first_name', 'last_name', 'company_name', 'area_code', 'primary_phone','street_address1',
                  'street_address2', 'zip_code', 'business_address']


class PaymentForm(forms.ModelForm):
    cardholder_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control required',
        'name': 'cardholder',
        'id': 'card-name'
    }))
    card_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control required',
        'name': 'card_number',
        'id': 'card-number'
    }))
    expired_month = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control required p-l-5 p-r-5 text-center',
        'name': 'month',
        'placeholder': 'MM',
        'id': 'card-month'
    }))
    expired_year = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control required p-l-5 p-r-5 text-center',
        'name': 'year',
        'placeholder': 'YY',
        'id': 'card-year'
    }))
    csc = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control required',
        'name': 'csc',
        'id': 'card-csc'
    }))

    class Meta:
        model = Payment
        fields = '__all__'


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'name': 'name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'name': 'email'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'subject'
    }))
    messsage = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'messsage'
    }))

    class Meta:
        model=Contact
        fields = '__all__'
