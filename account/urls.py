from django.urls import path, include
from .views import  Signin, Signup, ProfileView,Profile, auth_views, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('signin/', Signin.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(next_page='signin'), name='signout'),
    path('update-profile/<int:pk>/', ProfileView.as_view(), name='update-profile'),
    path('profile/', Profile.as_view(), name='profile'),
    path('change-password/', auth_views.as_view(), name='change-password'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    ]


