from django.contrib import admin
from django.urls import path
from app.views import registration_page, login_page, dashboard, add_edit_admission, \
        hospital_dashboard,hospital_payment_page,admission_history_page,carecenter_dashboard, \
        carecenter_payment_page,user_logout,dashboard,hospital_login_page,hospital_patient_details,carecenter_login_page,carecenter_patient_details,contact_page

urlpatterns = [
    path('register/', registration_page, name="register"),
    path('login/', login_page, name="login"),
    path("logout/",user_logout,name="logout"),
    path("dashboard/",dashboard,name="dashboard"),
    path('admission/', add_edit_admission, name="admission"),
    path('admission/<pk>/', add_edit_admission, name="admission"),
    path('admission/<pk>/hospitals', hospital_dashboard, name="hospitals"),
    path('admission/<a_id>/<h_id>/hospital/payment', hospital_payment_page, name="payment"),
    path('admission/<a_id>/<c_id>/carecenter/payment', carecenter_payment_page, name="carecenter-payment"),
    path('adm/history/', admission_history_page, name="admission-history"),
    path('admission/<pk>/carecenters', carecenter_dashboard, name="carecenters"),
    path('hospital/login/', hospital_login_page, name="hospital-login"),
    path('hospital/<pk>/details', hospital_patient_details, name="hospital-details"),
    path('carecenter/login/', carecenter_login_page, name="carecenter-login"),
    path('carecenter/<pk>/details', carecenter_patient_details, name="carecenter-details"),
    path('contacts', contact_page, name="contacts"),
    
]