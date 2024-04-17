from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponse, JsonResponse
from api.serializers import CompanySerializer, VacancySerializer
from .models import Company, Vacancy
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt 
import json
from rest_framework.decorators import api_view 
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



#FBV
@api_view(["GET","POST"])
def get_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =  CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()#insert data...
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["GET", "PUT","DELETE"])
def get_company_by_id(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e :
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    # ошибка 404
    if request.method == "GET":
        serializer =  CompanySerializer(company)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = CompanySerializer(
            instance = company,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()# update data...
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method  == 'DELETE':
        company.delete()
        return Response({"deleted": True})










def get_vacancies_by_companies(request, pk):
    # ошибка 404
    company = Company.objects.get(pk=pk)
    vacancies = Vacancy.objects.filter(company=company)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe = False)




#CBV

class VacancyListAPIView(APIView):
    def get(sef, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)



    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancyDetailAPIView(APIView):
    def get(self, request, pk=None):
        try:
            vacancy = Vacancy.objects.get(id=pk)
        except Vacancy.DoesNotExist as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
        
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    
    def put(self, request,pk=None):
        try:
            vacancy = Vacancy.objects.get(id=pk)
        except Vacancy.DoesNotExist as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
        
        serializer = VacancySerializer(instance=vacancy, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request,pk=None):
        try:
            vacancy = Vacancy.objects.get(id=pk)
        except Vacancy.DoesNotExist as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
        
        vacancy.delete()
        return Response({"deleted": True})

















# def get_vacancies(request):
#     # ошибка 404
#     if request.method == "GET":
#         vacancies = Vacancy.objects.all()
#         vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#         return JsonResponse(vacancies_json , safe = False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         vacancies = Vacancy.objects.create(name=data.data("name"))
#         return JsonResponse(vacancies.to_json)

# def get_vacancy_by_id(request, pk):
#     # ошибка 404
#     try:
#         vacancy = Vacancy.objects.get(id=pk)
#     except Vacancy.DoesNotExist as e :
#         # return JsonResponse({"error": str(e)})
#         raise Http404
    


#     if request.method == "GET":
#         return JsonResponse(vacancy.to_json())
#     elif request.method == "PUT":
#         data = json.loads(request.body)
#         vacancy.name = data.get("name")
#         vacancy.save()
#         return JsonResponse(vacancy.to_json)
#     elif request.method == "DELETE":
#         vacancy.delete()
#         return JsonResponse({"deleted": True})


def get_top_ten(request):
    vacancies = Vacancy.objects.order_by("-salary").all()[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)