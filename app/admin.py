from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Admission, HospitalPatientDetails, CareCenterPatientDetails, UserBookedAdmissionHistory

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username","password","full_name",'email', 'is_staff', 'is_active','date_joined','phone_number')
    list_filter = ("username","full_name",'email', 'is_staff', 'is_active','date_joined','phone_number')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','date_joined')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


from administrator.models import Hospital
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Admission)
admin.site.register(HospitalPatientDetails)
admin.site.register(CareCenterPatientDetails)
admin.site.register(UserBookedAdmissionHistory)