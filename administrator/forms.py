from django import forms
from administrator.models import Hospital,Carecenter

class HospitalForm(forms.ModelForm):
    description = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows': 4, 'cols': 180}))
    class Meta:
        model = Hospital
        fields = "__all__"

class CarecenterForm(forms.ModelForm):
    description = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows': 4, 'cols': 180}))
    class Meta:
        model = Carecenter
        fields = "__all__"
