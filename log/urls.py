from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('registrate/',views.RegistrationView.as_view()),
    path('login/', views.CustomAuthTokenView.as_view()),
    path('edit/', views.EditView.as_view()),
    path('add/balance/', views.AddBalanceView.as_view()),
]