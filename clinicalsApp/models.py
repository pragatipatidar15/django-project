from django.db import models

# Create your models here.
class Patient(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    age=models.IntegerField()
    
    
class ClinicalsData(models.Model):
    COMPONENT_NAMES=[('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentName=models.CharField(choices=COMPONENT_NAMES,max_length=20)
    componentValue=models.CharField(max_length=20)
    # for current data and time we use auto_now_add=true
    measuredDateTime=models.DateTimeField(auto_now_add=True)
    # one to many mapping between patient ------> clinicalData
    patient= models.ForeignKey(Patient,on_delete=models.CASCADE)
