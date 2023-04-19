from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path("companies/", views.company_list),
    path("companies/<int:id>/", views.company_detail),
    path("companies/<int:company_id>/vacancies/", views.vacancy_list_by_company),
    path("vacancies/", views.vacancy_list),
    path("vacancies/<int:vacancy_id>/", views.vacancy_detail),
    path("vacancies/top_ten/", views.top_ten),
]