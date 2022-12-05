from django import forms
from clinicalsApp.models import ClinicalsData,Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model=ClinicalsData
        fields='__all__'
