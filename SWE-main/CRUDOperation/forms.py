from django import forms
from CRUDOperation.models import SpecType
from CRUDOperation.models import EmpModel
from CRUDOperation.models import Patient

class SpecForms(forms.ModelForm):
    class Meta:
        model = SpecType
        fields = "__all__"

class Empforms(forms.ModelForm):
    class Meta:
        model = EmpModel
        fields = "__all__"

class PatientForms(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

