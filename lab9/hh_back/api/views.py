from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponse, JsonResponse
from .models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt 
import json

# def index(request):
# 	return HttpResponse("Hello, World! EMPTY PROJECT")



@csrf_exempt
def get_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe = False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(name=data.data("name"))
        return JsonResponse(company.to_json)

@csrf_exempt
def get_company_by_id(request, pk):
    company = Company.objects.get(id=pk)
    # ошибка 404
    if request.method == "GET":
        return JsonResponse(company.to_json())
    elif request.method == "PUT":
        data = json.loads(request.body)
        company.name = data.get("name")
        company.save()
        return JsonResponse(company.to_json)
    elif request.method  == 'DELETE':
        company.delete()
        return JsonResponse({"deleted": True})

def get_vacancies_by_companies(request, pk):
    # ошибка 404
    company = Company.objects.get(pk=pk)
    vacancies = Vacancy.objects.filter(company=company)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe = False)



def get_vacancies(request):
    # ошибка 404
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json , safe = False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vacancies = Vacancy.objects.create(name=data.data("name"))
        return JsonResponse(vacancies.to_json)

def get_vacancy_by_id(request, pk):
    # ошибка 404
    vacancy = Vacancy.objects.get(id=pk)
    if request.method == "GET":
        return JsonResponse(vacancy.to_json())
    elif request.method == "PUT":
        data = json.loads(request.body)
        vacancy.name = data.get("name")
        vacancy.save()
        return JsonResponse(vacancy.to_json)
    elif request.method == "DELETE":
        vacancy.delete()
        return JsonResponse({"deleted": True})


def get_top_ten(request):
    vacancies = Vacancy.objects.order_by("-salary").all()[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)