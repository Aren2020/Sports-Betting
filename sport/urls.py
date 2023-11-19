from django.urls import path
from . import views

urlpatterns = [
    path('sections/',views.SectionListView.as_view()),
    path('games/<slug:section>/',views.GameListView.as_view(),),
    path('games/<slug:section>/<int:pk>/',views.GameDetailView.as_view()),
    path('news/<slug:section>/', views.NewsView.as_view()),
]