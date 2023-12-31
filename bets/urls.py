from django.urls import path
from . import views

urlpatterns = [
    path('', views.BetListView.as_view()),
    path('winner/', views.BetWinnerView.as_view()),
    path('create/', views.BetCreateView.as_view()),
]