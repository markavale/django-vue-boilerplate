from django.urls import path,include
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView, LoginView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', include('dj_rest_auth.registration.urls'), name='register'),
    path('registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
