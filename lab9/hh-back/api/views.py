import json

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, JsonResponse
from api.models import Company, Vacancy


# Create your views here.
def get_companies(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies]
    return JsonResponse(companies_json, safe=False)


def get_one_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'Product not found'}, status=400)
    return JsonResponse(company.to_json())


def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def get_one_vacancy(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    vacancy_get = vacancy.to_json()
    return JsonResponse(vacancy_get)


def get_companies_vacancies(request, id):
    vacancy = Vacancy.objects.filter(company=id)
    vacancy_json = [v.to_json() for v in vacancy]
    return JsonResponse(vacancy_json, safe=False)


def get_top_ten(request):
    vacancy = Vacancy.objects.all()
    vacancy_json = [v.to_json() for v in vacancy]
    return JsonResponse(vacancy_json[:10], safe=False)