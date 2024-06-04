from django.shortcuts import render
from administrator.forms import HospitalForm, CarecenterForm
from administrator.models import Hospital, Carecenter
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import date
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from app.models import CustomUser
from app.models import HospitalPatientDetails,Admission,CareCenterPatientDetails

# Create your views here.

def admin_dashboard(request):
    context = {}
    context["hospital_count"] = Hospital.objects.all().count()
    context["carecenter_count"] = Carecenter.objects.all().count()
    context["registered_user_count"] = CustomUser.objects.all().count()
    context["hospital_patient_count"] = HospitalPatientDetails.objects.all().count()
    context["carecenter_patient_count"] = CareCenterPatientDetails.objects.all().count() 
    return render(request, 'admin_dashboard.html', {"context":context})

def add_hospital(request):
    if request.method=="POST":
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage-hospital'))
    else:
        form = HospitalForm(request.GET)

    return render(request, 'add_edit_hospital_page.html', {'form': form})

def edit_hospital(request,pk):
    obj = Hospital.objects.get(id=pk)
    print(obj)
    hospital_detail_form = HospitalForm(request.POST or None, instance = obj)
    if hospital_detail_form.is_valid():
        new_form = hospital_detail_form.save(commit=False)
        new_form.updated=timezone.now()
        new_form.save()
        return HttpResponseRedirect(reverse('manage-hospital'))

    return render(request, 'add_edit_hospital_page.html', {'form': hospital_detail_form})    

def manage_hospital(request):
    name = request.GET.get('hosp')
    city = request.GET.get('city')
    state = request.GET.get('state')
    if name or city or state:
        hospital_list = Hospital.objects.filter(Q(name__icontains=name)&Q(state__icontains=state)&Q(city__icontains=city)).order_by('name')
    else:
        hospital_list = Hospital.objects.all().order_by('name')
    state_list = set(list(hospital_list.values_list('state',flat=True)))
    city_list = set(list(hospital_list.values_list('city',flat=True)))
    paginator = Paginator(hospital_list, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'hospital_listing_page.html', {'page_obj': page_obj,"hospital_obj":hospital_list,"states":state_list,"city":city_list})

def add_carecenter(request):
    if request.method=="POST":
        form = CarecenterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manage-carecenter'))
    else:
        form = CarecenterForm(request.GET)

    return render(request, 'add_edit_care_center_page.html', {'form': form})

def edit_carecenter(request,pk):
    obj = Carecenter.objects.get(id=pk)
    carecenter_detail_form = CarecenterForm(request.POST or None, instance = obj)
    if carecenter_detail_form.is_valid():
        new_form = carecenter_detail_form.save(commit=False)
        new_form.updated=timezone.now()
        new_form.save()
        return HttpResponseRedirect(reverse('manage-carecenter'))

    return render(request, 'add_edit_care_center_page.html', {'form': carecenter_detail_form})    

def manage_carecenter(request):
    name = request.GET.get('hosp')
    city = request.GET.get('city')
    state = request.GET.get('state')
    if name or city or state:
        carecenter_list = Carecenter.objects.filter(Q(name__icontains=name)&Q(state__icontains=state)&Q(city__icontains=city)).order_by('name')
    else:
        carecenter_list = Carecenter.objects.all().order_by('name')
    state_list = set(list(carecenter_list.values_list('state',flat=True)))
    city_list = set(list(carecenter_list.values_list('city',flat=True)))
    paginator = Paginator(carecenter_list, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'care_center_listing_page.html', {'page_obj': page_obj,"carecenter_obj":carecenter_list,"states":state_list,"city":city_list})


def manage_admission(request):
    admission = Admission.objects.filter(status=True)
    paginator = Paginator(admission, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admission_listing_page.html', {'page_obj': page_obj})