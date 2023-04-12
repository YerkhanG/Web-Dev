from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path("companies/", views.get_companies),
    path("companies/<int:id>/", views.get_one_company),
    path("companies/<int:id>/vacancies/", views.get_companies_vacancies),
    path("vacancies/", views.get_vacancies),
    path("vacancies/<int:id>/", views.get_one_vacancy),
    path("vacancies/top_ten/", views.get_top_ten),
]