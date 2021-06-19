from django.urls import path
from .views import *

urlpatterns = [
    path('departapi/',departmentapi.as_view()),
    path('departapi/<int:pk>',Departmentapi.as_view()),
    path('employeeapi/',employeeapi.as_view()),
    path('employeeapi/<int:pk>',Employeeapi.as_view()),
    path('searchbydepartment/<int:pk>/', departsearchapi.as_view()),
    path('register/',RegisterUser.as_view()),
]