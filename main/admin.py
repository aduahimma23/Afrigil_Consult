from django.contrib import admin
from .models import *


admin.site.register(Contact)
admin.site.register(BookFlight)

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

@admin.register(ChangeContact)
class ChangeContactAdmin(admin.ModelAdmin):
    list_display = ("office", "mobile", "email")
    search_fields = ("office", "email")

@admin.register(Passport)
class passportAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'father', 'mother', 'grand_parent', 'guarantor', 'declaration', 'passportapplication', 'witness')
    search_fields = ('applicant__surname', 'applicant__first_name', 'applicant__national_ID_no')

@admin.register(PassportApplicantDetails)
class PassportApplicantDetailsAdmin(admin.ModelAdmin):
    list_display = ['applicant_name', 'father_name', 'mother_name', 'guarantor_name', 'witness_name', 'date_created']
    search_fields = ['applicant__first_name', 'applicant__surname', 'father__father_name', 'mother__mother_name', 'guarantor__full_name', 'witness__full_name', 'date_created']
