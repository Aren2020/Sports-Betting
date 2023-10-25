from django.urls import path
from . import views

urlpatterns = [
    path('sections/',views.SectionListView.as_view()),
    path('games/',views.GameListView.as_view()),
]