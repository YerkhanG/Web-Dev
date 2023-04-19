import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from api.models import Company, Vacancy
from api.serializers import CompanySerializer1, CompanySerializer2 , VacancySerializer1 , VacancySerializer2

# CRUD - CRATE, READ, UPDATE, DELETE

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer1(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        company_name = data.get('name', '')
        company = Company.objects.create(name=company_name)
        return JsonResponse(company.to_json())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_company_name = data.get('name', company.name)
        # desc = data.get('desc', company.desc)
        company.name = new_company_name
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [p.to_json() for p in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        vacancy_name = data.get('name', '')
        vacancy = Vacancy.objects.create(name=vacancy_name)
        return JsonResponse(vacancy.to_json())


@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_vacancy_name = data.get('name', vacancy.name)
        # desc = data.get('desc', company.desc)
        vacancy.name = new_vacancy_name
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})


# def top_ten(request):
#     vacancies = Vacancy.objects.all().order_by('-salary')[:10]

#     # Create a list of dictionaries to represent each vacancy as a JSON object
#     vacancy_list = []
#     for vacancy in vacancies:
#         vacancy_dict = {
#             'id': vacancy.id,
#             'title': vacancy.name,
#             'description': vacancy.description,
#             'salary': vacancy.salary
#         }
#         vacancy_list.append(vacancy_dict)

#     # Return a JSON response with the sorted list of vacancies
#     return JsonResponse(vacancy_list, safe=False)
def top_ten(request):
    vacancy = Vacancy.objects.all()
    serializer = VacancySerializer2(vacancy)
    return JsonResponse(serializer.data[:10], safe=False)
def vacancy_list_by_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        vacancy = Vacancy.objects.filter(company=company)
        vacancy_json = [v.to_json() for v in vacancy]
        return JsonResponse(vacancy_json, safe=False)