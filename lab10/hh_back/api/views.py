from urllib import response
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from api.models import Company, Vacancy
from rest_framework import status
from api.serializers import CompanySerializer, VacancySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view 

# Create your views here.
@api_view(["GET","POST"])
def company_list(request):
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
def company_details(request, id):
    try:
        company = Company.objects.get(id=id)
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


def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=404)
    
    vacancies = Vacancy.objects.filter(company=company)
    serializer = VacancySerializer(vacancies, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)



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
    


def vacany_top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)
