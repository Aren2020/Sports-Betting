from django.urls import path
from . import views

urlpatterns = [
    path('registrate/',views.RegistrationView.as_view()),
]