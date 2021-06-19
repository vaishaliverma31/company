from django.db import models

# Create your models here.
class department(models.Model):
    name_of_department=models.CharField(max_length=200)
    cabine_alloted=models.IntegerField(default=0)
    def __str__(self):
        return self.name_of_department
class employee(models.Model):
    name_of_employ=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    date_of_join=models.DateField()
    department_aloted=models.ForeignKey(department,on_delete=models.CASCADE)
    no_of_fruits=models.IntegerField(default=0)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name_of_employ
