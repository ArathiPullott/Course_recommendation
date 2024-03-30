from django.urls import path
from .views import search_courses_by_subject

urlpatterns = [
    path('',search_courses_by_subject, name='search_courses_by_subject'),
    # path('', views.search_form, name='search_form'),
    # path('', views.search_results, name='search_results'),
]