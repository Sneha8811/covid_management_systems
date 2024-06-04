from django.shortcuts import render
from app.forms import CustomUserCreationForm, Loginform, AdmissionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from administrator.models import Hospital,SeatAvailabilty,HospitalSignup,Carecenter,CareCenterSignup
from app.models import Admission,CustomUser,HospitalPatientDetails,CareCenterPatientDetails,UserBookedAdmissionHistory
from django.core.paginator import Paginator
from django.db.models import Q
import requests


# Create your views here.
def registration_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            print(form.cleaned_data)
            password = form.cleaned_data['password1']
            users = form.save()    
            users.set_password(request.POST.get("password1"))
            users.save()
            return HttpResponseRedirect(reverse('login'))
        return render(request,"registration.html",{'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request,"registration.html",{'form':form})

def login_page(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('admission'))
        return render(request, 'login.html', {'form': form})
    else:
        form = Loginform()
        return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard'))


def dashboard(request):
    state=request.GET.get("state","Tamil Nadu")
    data = requests.get("https://data.covid19india.org/state_district_wise.json").json()
    dashboard_data = []
    state_list = [ i for i,j in data.items()]
    for dist,dist_value in data[state]["districtData"].items():
        dashboard_data.append({"name":dist,"value":[dist_value['active'],dist_value['confirmed'],dist_value['deceased'],dist_value['recovered']]})

    return render(request, 'corona_dashboard.html', {'data':dashboard_data,"state_list":state_list,"selected_state":state})
@login_required
def add_edit_admission(request,pk=None):
    u_mail = request.user
    user_obj = CustomUser.objects.get(email=u_mail)
    user_id = user_obj.pk
    print(user_id,pk)
    if pk:
        obj = Admission.objects.get(id=pk)
        print(obj)
        admission_detail_form = AdmissionForm(request.POST or None, instance = obj)
        if request.method == "POST":
            print(admission_detail_form.errors)
            if admission_detail_form.is_valid():
                admission_detail_form.save()
                if request.POST.get("severity") == "High":
                    return HttpResponseRedirect(reverse('hospitals',kwargs={'pk':pk}))
                return HttpResponseRedirect(reverse('carecenters',kwargs={'pk':pk}))
            return render(request, 'admission.html', {'form': admission_detail_form})
        
        return render(request, 'admission.html', {'form': admission_detail_form})
    else:
        if request.method == "POST":
            print(request.POST)
            form = AdmissionForm(request.POST)
            print(form.errors)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user_id=user_obj
                new_form.save()
                if request.POST.get("severity") == "High":
                    return HttpResponseRedirect(reverse('hospitals',kwargs={'pk':new_form.id}))
                return HttpResponseRedirect(reverse('carecenters',kwargs={'pk':new_form.id}))
            return render(request, 'admission.html', {'form': form})
        else:
            form = AdmissionForm()

        return render(request, 'admission.html', {'form': form})


def hospital_dashboard(request,pk):
    city = ""
    state = ""
    admission = Admission.objects.filter(id=pk).values("city","state")
    if admission:
        city = admission[0]['city']
        state = admission[0]['state']
    hospital_list = Hospital.objects.filter(Q(state__icontains=state)&Q(city__icontains=city)).order_by('name')
    paginator = Paginator(hospital_list, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(hospital_list)
    return render(request, 'admission_hospitals.html', {'page_obj': page_obj,"hospital_obj":hospital_list,"addmission_id":pk})

def carecenter_dashboard(request,pk):
    city = ""
    state = ""
    admission = Admission.objects.filter(id=pk).values("city","state")
    print(admission)
    if admission:
        city = admission[0]['city']
        state = admission[0]['state']
    print(city)
    carecenter_list = Carecenter.objects.filter(Q(state__icontains=state)&Q(city__icontains=city)).order_by('name')
    paginator = Paginator(carecenter_list, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admission_carecenter.html', {'page_obj': page_obj,"hospital_obj":carecenter_list,"addmission_id":pk})



def carecenter_payment_page(request,a_id,c_id):
    carecenter_name = Carecenter.objects.filter(id=c_id).values("name")[0]['name']
    if request.method=="POST":
        available_bed_count = SeatAvailabilty.objects.filter(carecenter_id=c_id).values('available_beds')[0]['available_beds']
        available_bed_count = available_bed_count - 1
        SeatAvailabilty.objects.filter(carecenter_id=c_id).update(available_beds=available_bed_count)
        available_bed_count = SeatAvailabilty.objects.filter(carecenter_id=c_id).values('available_beds')[0]['available_beds']
        admission_obj = Admission.objects.filter(id=a_id).values()
        for data in admission_obj:
            CareCenterPatientDetails.objects.create(
                carecenter_id=c_id,
                username=data['patient_name'],
                email=data['email'],
                age=data['age'],
                phone_number=data["phone_number"],
                gender=data["gender"],
                address=data['address'],
                relative_address=data["relative_address"],
                relative_contact=data["relative_contact"],
                serverity=data["severity"],
                aadhaar_number=data["aadhaar_number"],
                bed_type="Without oxygen",
                status=True,
            )
        Admission.objects.filter(id=a_id).update(status=True)
        user_mail = request.user
        user_obj = CustomUser.objects.get(email=user_mail)
        user_id = user_obj.pk
        if not UserBookedAdmissionHistory.objects.filter(admission_id=a_id,user_id=user_id,carecenter_id=c_id).exists():
            UserBookedAdmissionHistory.objects.create(admission_id=a_id,user_id=user_id,carecenter_id=c_id)
        return HttpResponseRedirect(reverse('admission-history'))

    return render(request, 'carecenter_payment_page.html', {'carecenter_name':carecenter_name})

def hospital_payment_page(request,a_id,h_id):
    bed_type = request.POST.get("bed_type")
    hospital_name = Hospital.objects.filter(id=h_id).values("name")[0]['name']
    if bed_type:
        if request.method=="POST":
            available_bed_count = SeatAvailabilty.objects.filter(hospital_id=h_id,bed_type=bed_type).values('available_beds')[0]['available_beds']
            available_bed_count = available_bed_count - 1
            SeatAvailabilty.objects.filter(hospital_id=h_id,bed_type=bed_type).update(available_beds=available_bed_count)
            available_bed_count = SeatAvailabilty.objects.filter(hospital_id=h_id,bed_type=bed_type).values('available_beds')[0]['available_beds']
            admission_obj = Admission.objects.filter(id=a_id).values()
            for data in admission_obj:
                HospitalPatientDetails.objects.create(
                   hospital_id=h_id,
                   username=data['patient_name'],
                   email=data['email'],
                   age=data['age'],
                   phone_number=data["phone_number"],
                   gender=data["gender"],
                   address=data['address'],
                   relative_address=data["relative_address"],
                   relative_contact=data["relative_contact"],
                   serverity=data["severity"],
                   aadhaar_number=data["aadhaar_number"],
                   bed_type=bed_type,
                   status=True,
                )
            Admission.objects.filter(id=a_id).update(status=True)
            user_mail = request.user
            user_obj = CustomUser.objects.get(email=user_mail)
            user_id = user_obj.pk
            if not UserBookedAdmissionHistory.objects.filter(admission_id=a_id,user_id=user_id,hospital_id=h_id).exists():
                UserBookedAdmissionHistory.objects.create(admission_id=a_id,user_id=user_id,hospital_id=h_id)
            return HttpResponseRedirect(reverse('admission-history'))

    return render(request, 'hospital_payment_page.html', {'hospital_name':hospital_name})

def admission_history_page(request):
    hospital_ids = []
    carecenter_ids = []
    user_mail = request.user
    user_obj = CustomUser.objects.get(email=user_mail)
    user_id = user_obj.pk
    hospitals_obj = UserBookedAdmissionHistory.objects.exclude(carecenter_id__isnull=False).filter(user_id=user_id).values()
    carecenter_obj = UserBookedAdmissionHistory.objects.exclude(hospital_id__isnull=False).filter(user_id=user_id).values()
    hos_booked_info = []
    care_booked_info = []

    for data in hospitals_obj:
        admission_obj = Admission.objects.filter(id=data['admission_id']).values()
        hospital_obj = admission_obj[0]
        hospital_obj['hospital_name'] = Hospital.objects.filter(id=data['hospital_id']).values("name")[0]['name']
        hospital_obj["bed_type"] = HospitalPatientDetails.objects.filter(username=admission_obj[0]['patient_name']).values("bed_type")[0]['bed_type']
        hos_booked_info.append(hospital_obj)
    for data in carecenter_obj:
        admission_obj = Admission.objects.filter(id=data['admission_id']).values()
        care_obj = admission_obj[0]
        care_obj['center_name'] = Carecenter.objects.filter(id=data['carecenter_id']).values("name")[0]['name']
        care_obj["bed_type"] = "Without oxygen"
        care_booked_info.append(care_obj)
   
    return render(request, 'admission_history_page.html',{"hos_booked_info":hos_booked_info,"care_info":care_booked_info})


def hospital_login_page(request):
    user_name = request.POST.get("user_name")
    password = request.POST.get("password")
    users = HospitalSignup.objects.filter(user_name=user_name,password=password).values()
    print(users)
    if users.exists():
        return HttpResponseRedirect(reverse('hospital-details',kwargs={'pk':users[0]["hospital_id"]}))
    return render(request, 'hospital_login.html',{})

def hospital_patient_details(request,pk):
    h_p = HospitalPatientDetails.objects.filter(hospital_id=pk)
    paginator = Paginator(h_p, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'hospital_patient.html',{"page_obj":h_p})

def carecenter_login_page(request):
    user_name = request.POST.get("user_name")
    password = request.POST.get("password")
    users = CareCenterSignup.objects.filter(user_name=user_name,password=password).values()
    print(users)
    if users.exists():
        return HttpResponseRedirect(reverse('carecenter-details',kwargs={'pk':users[0]["carecenter_id"]}))
    return render(request, 'carecenter_login.html',{})

def carecenter_patient_details(request,pk):
    h_p = CareCenterPatientDetails.objects.filter(carecenter_id=pk)
    print(h_p)
    paginator = Paginator(h_p, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'carecenter_patient.html',{"page_obj":h_p})

def contact_page(request):
    return render(request, 'contacts.html',{})
