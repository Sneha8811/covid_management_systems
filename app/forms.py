from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from app.models import CustomUser, Admission
from django.contrib.auth import authenticate


class   CustomUserCreationForm(UserCreationForm):


    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Your UserName'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control",'placeholder': 'Your Email'}))

    full_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Your FullName'}))

    phone_number = forms.CharField(max_length=10,widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Your Phone Number'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder': 'Your Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder': 'Your Confirm password'}))

    class Meta:
        model = CustomUser
        fields = ('username','full_name','email','phone_number','password1','password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class Loginform(forms.ModelForm):

    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", 'Placeholder':'Enter your Email id'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'Placeholder':'Enter your Password'}))

    class Meta():

        model = CustomUser

        fields = ('email','password')

    def clean(self):

        cleaned_data = super().clean()

        email = self.cleaned_data.get('email')

        password = self.cleaned_data.get("password")

class AdmissionForm(forms.ModelForm):
    GENDER_CHOICES=[('Male','Male'),
         ('Female','Female')]
    
    SEVERITY_CHOICES=[('High','High'),
         ('Low','Low')]

    patient_name = forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Patient Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", 'Placeholder':'Enter your Email id'}))
    phone_number = forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Your Phone Number'}))
    relative_contact = forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Emergency Number'}))
    gender = forms.ChoiceField(required=True,choices=GENDER_CHOICES, widget=forms.RadioSelect,label="Gender")
    severity = forms.ChoiceField(required=True,choices=SEVERITY_CHOICES, widget=forms.RadioSelect,label="Severity")
    age  =  forms.IntegerField(required=True,widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Your Age'}))
    aadhaar_number = forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Your Aadhaar Number'}))
    address = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows': 3, 'cols': 43}))
    relative_address = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows': 3, 'cols': 43}))
    
        
    class Meta():
        model = Admission
        fields = ("patient_name","email","phone_number","relative_contact","address","relative_address","age","aadhaar_number",'gender','severity','city','state')