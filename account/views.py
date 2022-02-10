from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from django.conf import settings
from django.views import View
from django.contrib.auth import logout, login
import stripe
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

stripe.api_key = "sk_test_51KP4XtKGdsOCaVQ79IKbR3h6tP7d3jZPiaXwWwuVFJWBr7jr828P83hGYzGuzreau2uS9H96UZuB6MzwkEKLSpZt00qLWZlVL0"


class Signin(LoginView, LoginRequiredMixin):
    template_name = 'account/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    success_message = "You Have Signin Successfully"

    def get_success_url(self):
        return reverse_lazy('home')


class Signup(CreateView):
    template_name = 'account/signup.html'
    form_class = SignUpForm
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):
        super(Signup, self).post(request)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        stripe.Customer.create(
            description=username,
            email=email,
        )
        return redirect('/account/signin/')

    success_url = reverse_lazy('home')


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'account/profile-update.html'


class auth_views(PasswordChangeView):
    template_name = 'account/change-password.html'
    success_url = '/'


class PasswordResetView(PasswordResetView):
    template_name = 'account/password-reset/password_reset.html'
    subject_template_name = 'account/password-reset/password_reset_subject.txt'
    email_template_name = 'account/password-reset/password_reset_email.html'

    # success_url='/login/'


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password-reset/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password-reset/password_reset_confirm.html'


class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password-reset/password_reset_complete.html'

    def get_success_url(self):
        return reverse_lazy('home')


class Profile(View):
    model = User

    def get(self, request):
        return render(request, 'account/profile.html')
