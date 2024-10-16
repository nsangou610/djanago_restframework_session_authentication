from django.urls import path
from userapp.views import RegistrationView, CheckAuthenticatedView, LoginView, UserDetailView, ChangePasswordView, DeleteAccountView, LogoutView

urlpatterns = [
    path('checkauth/', CheckAuthenticatedView.as_view(), name='check_auth'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('delete/', DeleteAccountView.as_view(), name='user_delete'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
