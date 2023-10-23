from django.urls import path
from . import views

urlpatterns = [
    path('section/',views.SectionListView.as_view()),
]