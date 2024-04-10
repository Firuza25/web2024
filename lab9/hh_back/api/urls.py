from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('companies/', views.get_companies),
    path('companies/<int:pk>/', views.get_company_by_id),
    path('companies/<int:pk>/vacancies/', views.get_vacancies_by_companies),
    path('vacancies/', views.get_vacancies),
    path('vacancies/<int:pk>/', views.get_vacancy_by_id),
    path('vacancies/top_ten/', views.get_top_ten),
]