from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from .form import *

def base(request):
    change_contact = ChangeContact.objects.first()
    social_media = SocialMediaHandle.objects.first()

    if request.method == "POST":
        news_form = NewsletterSubscriptionForm(request.POST)
        try:
            if news_form.is_valid():
                news_form.save()
                messages.success(request, 'You have successfully signed up for the newsletter.')
                return redirect('newsletter_signup')
            else:
                messages.error(request, 'There was an error with your submission. Please try again.')
        except Exception as err:
            messages.error(request, f"An error occured {err}")
    else:
        news_form = NewsletterSubscriptionForm()

    return render(request, "main/base.html", {"change_contact": change_contact, "social_media": social_media, "news_form": news_form})

def home(request):
    holiday_places = HolidayPlaces.objects.all()[:4]
    scholarships  = ScholarshipLink.objects.all()[:5]
    guides = Guide.objects.all()
    packages = Package.objects.all()
    destinations = Destination.objects.all()[:6]
   

    return render(request, "main/index.html", {"holiday_places": holiday_places, "guides": guides,
                        "scholarships": scholarships, "packages": packages, "destinations": destinations, 
                        })

def contact(request):
    change_contact = ChangeContact.objects.first()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        try:
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Your message has been sent successfully.')
                return redirect("contact")
            else:
                messages.error(request, 'There was an error in your form. Please correct the errors below.')
        except Exception as err:
            messages.error(request, f"An error occured {err}")
    else:
            contact_form = ContactForm()

    return render(request, "main/contact.html", {"contact_form": contact_form, "change_contact": change_contact})

def about(request):
    return render(request, "main/about.html")

def service(request):
    return render(request, "main/service.html", )

# @login_required(login_url='/account/login/')
def passport(request):
    if request.method == 'POST':
        applicant_form = ApplicantForm(request.POST)
        father_form = FatherForm(request.POST)
        mother_form = MotherForm(request.POST)
        grandparent_form = GrandParentForm(request.POST)
        guarantor_form = GuarantorForm(request.POST)
        declaration_form = DeclarationForm(request.POST)
        passportconsent_form = PassportConsentForm(request.POST)
        passportapplication_form = PassportApplicationForm(request.POST)
        witness_form = WitnessForm(request.POST)
        document_form = DeclarationForm(request.POST)

        if all([applicant_form.is_valid(), father_form.is_valid(), mother_form.is_valid(), grandparent_form.is_valid(), 
            guarantor_form.is_valid(), declaration_form.is_valid(), passportconsent_form.is_valid(), 
            passportapplication_form.is_valid(), witness_form.is_valid(), document_form.is_valid()
        ]):
            applicant_form.save(commit=False)
            father_form.save(commit=False)
            mother_form.save(commit=False)
            grandparent_form.save(commit=False)
            guarantor_form.save(commit=False)
            declaration_form.save(commit=False)
            passportconsent_form.save(commit=False)
            passportapplication_form.save(commit=False)
            witness_form.save(commit=False)
            document_form.save(commit=False)

            messages.success("Application Submitted")
            return redirect('success_url')
        
    else:
        applicant_form = ApplicantForm()
        father_form = FatherForm()
        mother_form = MotherForm()
        grandparent_form = GrandParentForm()
        guarantor_form = GuarantorForm()
        declaration_form = DeclarationForm()
        passportconsent_form = PassportConsentForm()
        passportapplication_form = PassportApplicationForm()
        document_form = DeclarationForm()
        witness_form = WitnessForm()

    return render(request, 'main/passport_form.html', 
                {'applicant_form': applicant_form, 'father_form': father_form, 
                    'mother_form': mother_form, 'grandparent_form': grandparent_form,
                    'guarantor_form': guarantor_form, 'declaration_form': declaration_form,
                    'passportconsent_form': passportconsent_form, "document_form": document_form,
                    'passportapplication_form': passportapplication_form, 'witness_form': witness_form
                })

# @login_required(login_url='/account/login/')
def birthcert(request):
    if request.method == "POST":
        birth_form = BirthCertificateForm(request.POST)
        try:
            if birth_form.is_valid():
                birth_form.save(commit=False)
                messages.success(request, "Form submitted successfully")
                return redirect("success_url")
            else:
                messages.error(request, "There were errors in the form, please correct them and try again.")
        except Exception as err:
            messages.error(request, f"Please provide the correct details: {err}")
    else:
        birth_form = BirthCertificateForm()
    
    return render(request, "main/birthcert.html", {"birth_form": birth_form})

# @login_required(login_url='/account/login/')
def bookflight(request):
    if request.method == "POST":
        booking_form = BookFlightForm(request.POST)
        try:
            if booking_form.is_valid():
                booking_form.save(commit=False)
                messages.success(request, "Flight successfully booked")
                return redirect("success_url")
            else:
                messages.error(request, "Check the form and try again")
        except Exception as err:
            messages.error(request, f"Fill all the fields")
    else:
        booking_form = BookFlightForm()

    return render(request, "main/booking.html", {"booking_form": booking_form})

def package(request):
    packages = Package.objects.all()

    return render(request, "main/package.html", {"packages": packages})

# @login_required(login_url='/account/login/')
def bookpackage(request):
    if request.method == "POST":
        package_form = PackageBookForm(request.POST)
        try:
            if package_form.is_valid():
                package_form.save(commit=False)
                messages.success(request, "Package booked successfully")
                return redirect("success_url")
            
        except Exception as e:
            messages.error(request, "Check the form")
    else:
        package_form = PackageBookForm()

    return render(request, "main/book_form.html", {"package_form": package_form})

@login_required(login_url='/account/login/')
def hotel_reserve(request):
    if request.method == "POST":
        hotel_reserve_form = HotelReservationFoorm(request.POST)
        try:
            if hotel_reserve_form.is_valid():
                hotel_reserve_form.save(commit=False)
                messages.success(request, "Hotel Reservation Successful")
                return redirect("success_url")
            
        except Exception as err:
            messages.error(request, f"Enter all the values accurately!{err}")
    
    else:
        hotel_reserve_form = HotelReservationFoorm()

    return render(request, "main/hotel_reserve.html", {"hotel_reserve_form": hotel_reserve_form})

# @login_required(login_url='/account/login/')
def scholarship_link(request):
    current_time = timezone.now().date()
    scholarships = ScholarshipLink.objects.filter(deadline__gte=current_time)

    return render(request, "main/scholar.html", {"scholarships": scholarships})