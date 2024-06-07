from django.contrib import admin
from .models import *


admin.site.register(Contact)
admin.site.register(Package)
admin.site.register(HolidayPlaces)

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

@admin.register(ScholarshipLinks)
class ScholarshipLinksAdmin(admin.ModelAdmin):
    list_display = ("country", "state", "institute_name",  "organization")
    search_fields = ("institute_name", "country", "state", "organization")
    list_editable = ("institute_name", "organization")

@admin.register(BirthCertificate)
class BirthCertificateAdmin(admin.ModelAdmin):
    list_display = ("first_name", "surname", "date_of_birth", "gender")
    search_fields = ("first_name", "surname", "date_of_birth", "gender")

@admin.register(VisaProcess)
class VisaProcessAdmin(admin.ModelAdmin):
    list_display = ("full_name", "country", "passport_number")
    list_display_links = [list_display[0],]
    search_fields = ("full_name", "country", "passport_number")
    list_editable = ("country", "passport_number")

@admin.register(HotelReservation)
class HotelReservationAdmin(admin.ModelAdmin):
    list_display = ("country", "city")
    search_fields = ("country", "city")

class SocialMediaHandlesAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.list_display_links = (self.list_display[0],)
        self.list_editable = [field for field in self.list_display if field != self.list_display[0]]
        super(SocialMediaHandlesAdmin, self).__init__(model, admin_site)

admin.site.register(SocialMediaHandles, SocialMediaHandlesAdmin)

@admin.register(BookFlight)
class BookFlightAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "departure_date", "return_date", "destination", "travel_type")
    search_fields = ("name", "destination", "travel_type")
    list_editable = ("destination", "return_date", "departure_date", "travel_type")

@admin.register(Guides)
class GuidesAdmin(admin.ModelAdmin):
    list_display = ( "created_at", "full_name", "destination")
    search_fields = ("full_name", "destination")
    list_editable = ( "full_name", "destination")