from django import forms
from CRUDOperation.models import EmpModel
from CRUDOperation.models import Patient

class Empforms(forms.ModelForm):
    class Meta:
        model = EmpModel
        fields = "__all__"

class PatientForms(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

