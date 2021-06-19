from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serialzires import *
from rest_framework.response import  Response
from datetime import date, datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from  rest_framework.views import  APIView

# Create your views here.
class departmentapi(ListCreateAPIView):
    queryset = department.objects.all()
    serializer_class = departserializers
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
class RegisterUser(APIView) :
    def post(self,request):
        serializer=userseializer(data=request.data)

        if not serializer.is_valid():
               print(serializer.errors)
               return ({'status':403,'errors':serializer.errors,'message':'something went wrong'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status':200,'payload':serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token),'message':'your data is saved'})





class Departmentapi(RetrieveUpdateDestroyAPIView):
    queryset = department.objects.all()
    serializer_class = departserializers


class employeeapi(ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employserializers
    def perform_create(self, serializer):
        global fruits
        serializer=self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            dept=self.request.data['department_aloted']
            print(type(dept))
            if dept>='2':
                fruits=10
                serializer.save(no_of_fruits=fruits)
            else:
                fruits=60
                serializer.save(no_of_fruits=fruits)

    def perform_create(self, serializer):
        global user_active

        TODAY=date.today()
        today_date=datetime.strftime(TODAY,'%d/%m/%y')
        print(today_date)

        serializer=self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            query=self.request.data['date_of_join']
            print(query)
            if query==today_date:
                      user_active=True
                      serializer.save(active=user_active)







class Employeeapi(RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employserializers




class departsearchapi(ListAPIView):
    queryset = employee.objects.all()
    serializer_class = employserializers

    def list(self, request, *args, **kwargs):
        Queryset=employee.objects.filter(department_aloted=self.kwargs["pk"])
        serializer=employserializers(Queryset,many=True)
        return Response(serializer.data)
