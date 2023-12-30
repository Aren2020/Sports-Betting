from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.BetCreateView.as_view()),
]