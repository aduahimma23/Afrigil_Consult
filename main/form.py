from django import forms
from .models import (Contact, Applicant, Father, Mother, GrandParent, Guarantor, 
                     Declaration, PassportConsent, PassportApplication, Witness,
                     VisaProcess, BirthCertificate, Document, BookFlight, PackageBook,
                    HotelReservation, NewsletterSubscription
                    )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here', 'rows': 4}),
        }


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-primary py-3 ps-4',
                'placeholder': 'Your email',
                'style': 'flex: 1;',
            }),
        }


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ameyaw'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emmanuel'}),
            'other_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other Name(Optional)'}),
            'date_of_birth': forms.DateInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'dd/mm/yy'}),
            'city_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Accra'}),
            'country_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ghana'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '158.2cm'}),
            'eye_colour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brown'}),
            'hair_colour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Black'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ghanaian'}),
            'marital_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select'}),
            'profession': forms.Select(attrs={'class': 'form-control', 'placeholder': 'TSelect'}),
            'previous_profession': forms.Select(attrs={'class': 'form-control', 'placeholder': 'If any'}),
            'national_ID_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '115587499'}),
            'social_security_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Social Security Number'}),
            'voters_ID_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Voter\'s ID Number'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Code'}),
            'country_of_residence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country of Residence'}),
            'suburb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Suburb'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House Number'}),
            'street_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Number'}),
            'digital_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digital Address'}),
            'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Address'}),
            'telephone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institution'}),
            'address': forms.TextInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Address'}),
            'period_from': forms.DateInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'Period From'}),
            'period_to': forms.DateInput(attrs={"type": "date", 'class': 'form-control', 'placeholder': 'Period To'}),
            'Dual_citizen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Dual Citizen'}),
        }

class FatherForm(forms.ModelForm):
    class Meta:
        model = Father
        fields = '__all__'
        widgets = {
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "FatherName",}),
            'living': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Living', "id": "living"}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Address'}),
            'residential_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residential Address'}),
            'home_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Town'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'id': 'phone_number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', "id": "email"}),
        }


class MotherForm(forms.ModelForm):
    class Meta:
        model = Mother
        fields = '__all__'
        widgets = {
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother\'s Name'}),
            'living': forms.Select(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Address'}),
            'residential_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residential Address'}),
            'home_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Town'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class GrandParentForm(forms.ModelForm):
    class Meta:
        model = GrandParent
        fields = '__all__'
        widgets = {
            'grand_parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Grand Parent\'s Name'}),
            'living': forms.Select(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Address'}),
            'residential_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residential Address'}),
            'home_town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Town'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class GuarantorForm(forms.ModelForm):
    class Meta:
        model = Guarantor
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'residential_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residential Address'}),
            'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Address'}),
            'telephone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone Number'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'date': forms.DateInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'Date'}),
        }

class DeclarationForm(forms.ModelForm):
    class Meta:
        model = Declaration
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'telephone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone Number'}),
            'date': forms.DateInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'Date'}),
        }

class PassportConsentForm(forms.ModelForm):
    class Meta:
        model = PassportConsent
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'telephone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephone Number'}),
            'date': forms.DateInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'Date'}),
        }

class PassportApplicationForm(forms.ModelForm):
    class Meta:
        model = PassportApplication
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'previous_passport_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Previous Passport Number'}),
            'date': forms.DateInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'Date'}),
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        widgets = {
            'document_type': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Document Number'}),
            'date_of_issue': forms.DateInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'Date of Issue'}),
            'place_of_issue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place of Issue'}),
        }

class WitnessForm(forms.ModelForm):
    class Meta:
        model = Witness
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'business_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Address'}),
            'business_phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Phone Number'}),
            'residential_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residential Address'}),
            'residential_phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residential Phone Number'}),
            'date': forms.DateInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'Date'}),
        }

class BirthCertificateForm(forms.ModelForm):
    class Meta:
        model = BirthCertificate
        fields = "__all__"

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'other_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other names (if any)'}),
            'date_of_birth': forms.TextInput(attrs={"type": "date", 'class': 'form-control datepicker', 'placeholder': 'Date of Birth'}),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'place of birth'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Father's Name"}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teaching'}),
            'religion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'region'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mother's Maiden Name"}),
            "ghana_card_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
        }

class BookFlightForm(forms.ModelForm):
    class Meta:
        model = BookFlight
        fields = "__all__"

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "travel_type": forms.Select(attrs={"class": "form-control"}),
            "departure_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "return_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "daparture_from": forms.TextInput(attrs={"class": "form-control"}),
            "destination": forms.TextInput(attrs={"class": "form-control"}),
            "travellers": forms.TextInput(attrs={"class": "form-control"}),
            "cabin_calss": forms.Select(attrs={"class": "form-control"}),
        }

class PackageBookForm(forms.ModelForm):
    class Meta:
        model = PackageBook
        fields = ("full_name", "contact")

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "contact": forms.TextInput(attrs={"class": "form-control", "placeholder": "Preferred contact"}),
        }


class HotelReservationFoorm(forms.ModelForm):
    class Meta:
        model = HotelReservation
        fields = "__all__"

        widgets = {
            "country": forms.Select(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "adults": forms.TextInput(attrs={"class": "form-control"}),
            "children": forms.TextInput(attrs={"class": "form-control"})
        }