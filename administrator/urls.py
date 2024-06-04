from django.contrib import admin
from django.urls import path
from administrator.views import add_hospital,edit_hospital,manage_hospital,add_carecenter,edit_carecenter,manage_carecenter,admin_dashboard,manage_admission

urlpatterns = [
    path('admin/dashboard', admin_dashboard, name="admin-dashboard"),
    path('admin/hospital/add', add_hospital, name="add-hospital"),
    path('admin/hospital/edit/<pk>', edit_hospital, name="edit-hospital"),
    path('admin/list/hospital', manage_hospital, name="manage-hospital"),
    path('admin/carecenter/add', add_carecenter, name="add-carecenter"),
    path('admin/carecenter/edit/<pk>', edit_carecenter, name="edit-carecenter"),
    path('admin/list/carecenter', manage_carecenter, name="manage-carecenter"),
    path('admin/list/admission', manage_admission, name="manage-admission"),
  

]