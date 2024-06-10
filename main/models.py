from django.db import models
from django.utils import timezone
from custom_account.models import CustomUser


CHOICE = {
    "Y": "YES",
    "N": "NO"
}
CHOICE_SELECTION = [(key, value) for key, value in CHOICE.items()]

MARITAL_STATUS_DICT = {
    'MA': 'Married', 'SI': 'Single',
    'DI': 'Divorced', 'WI': 'Widowed',
}
MARITAL_STATUS_CHOICES = [(key, value) for key, value in MARITAL_STATUS_DICT.items()]

GENDER = {
    "MA": "Male", "FA": "Female", "OT": "Others"
}
GENDER_CHOICE = [(key, value) for key, value in GENDER.items()]

PROFESSION_DICT = {
        'ENG': 'Engineer', 'DOC': 'Doctor', 'TCH': 'Teacher', 'ART': 'Artist', 'LWR': 'Lawyer',
        'DEV': 'Developer', 'NRS': 'Nurse', 'ACC': 'Accountant', 'MGR': 'Manager', 'SCI': 'Scientist',
        'MUS': 'Musician', 'ATH': 'Athlete', 'CHE': 'Chef', 'WRD': 'Writer', 'PHO': 'Photographer',
        'DSG': 'Designer', 'ENT': 'Entrepreneur', 'ARC': 'Architect', 'PLB': 'Plumber', 'ELC': 'Electrician',
        'MEC': 'Mechanic', 'PIL': 'Pilot', 'AST': 'Astronaut', 'FIR': 'Firefighter', 'POL': 'Police Officer',
        'JRN': 'Journalist', 'TRD': 'Trader', 'PRG': 'Programmer', 'TXI': 'Taxi Driver', 'HRM': 'HR Manager',
        'MKD': 'Marketing Director',
    }
PROFESSION_CHOICES = [(key, value) for key, value in PROFESSION_DICT.items()]

VISA_TYPE = {
    "B": "BUSINESS", "T": "Tourist Visa(T)", "E": "Employment Visa(E)",
    "S": "Student Visa (S)", "TR": "Transit Visa(TR)", "J": "Journalist Visa(J)",
    "Med": "Medical Visa(Med)", "C": "Conference(C)", "X": "Entry(X) visa"
}

VISA_TYPE_CHOICE = [(key, value) for key, value in VISA_TYPE.items()]

ECONOMY = 'Economy'
BUSINESS = 'Business'
FIRST_CLASS = 'First Class'
CABIN_CLASS_CHOICES = [(ECONOMY, 'Economy'), (BUSINESS, 'Business'), (FIRST_CLASS, 'First Class'),]

ONE_WAY = "OW"
RETURN = "RT"
SELECT_TYPE = [(ONE_WAY, "One Way"), (RETURN, "Return Trip"),]

COUNTRIES = {
"Afghanistan": "Afghanistan", "Albania": "Albania", "Algeria": "Algeria", "Andorra": "Andorra", 
"Angola": "Angola", "Antigua and Barbuda": "Antigua and Barbuda", "Argentina": "Argentina",
"Armenia": "Armenia", "Australia": "Australia", "Austria": "Austria", "Azerbaijan": "Azerbaijan",
"The Bahamas": "The Bahamas", "Bahrain": "Bahrain", "Bangladesh": "Bangladesh", "Barbados": "Barbados",
"Belarus": "Belarus", "Belgium": "Belgium", "Belize": "Belize", "Benin": "Benin",
"Bhutan": "Thimphu", "Bolivia": "La Paz, Sucre", "Bosnia and Herzegovina": "Sarajevo",
"Botswana": "Botswana", "Brazil": "Brazil", "Brunei": "Brunei", "Bulgaria": "Bulgaria",
"Burkina Faso": "Burkina Faso", "Burundi": "Burundi", "Cambodia": "Cambodia", "Cameroon": "Cameroon",
"Canada": "Canada", "Cape Verde": "Cape Verde", "Central African Republic": "Central African Republic", "Chad": "Chad",
"Chile": "Chile", "China": "China", "Colombia": "Colombia", "Comoros": "Comoros", "Republic of the Congo": "Republic of the Congo",
"Democratic Republic of the Congo": "Democratic Republic of the Congo", "Costa Rica": "Costa Rica", "Cote d Ivoire": "Cote d Ivoire",
"Croatia": "Croatia", "Cuba": "Cuba", "Cyprus": "Cyprus", "Czech Republic": "Czech Republic", "Denmark": "Denmark",
"Djibouti": "Djibouti", "Dominica": "Dominica", "Dominican Republic": "Dominican Republic", "East Timor": "East Timor",
"Ecuador": "Ecuador", "Egypt": "Egypt", "El Salvador": "El Salvador", "Equatorial Guinea": "Equatorial Guinea",
"Eritrea": "Eritrea", "Estonia": "Estonia", "Ethiopia": "Ethiopia", "Fiji": "Fiji", "Finland": "Finland",
"France": "France", "Gabon": "Gabon", "The Gambia": "The Gambia", "Georgia": "Georgia", "Germany": "Germany",
"Ghana": "Ghana", "Greece": "Greece", "Grenada": "Grenada", "Guatemala": "Guatemala",
"Guinea": "Guinea", "Guinea-Bissau": "Guinea-Bissau", "Guyana": "Guyana", "Haiti": "Haiti",
"Honduras": "Honduras", "Hungary": "Hungary", "Iceland": "Iceland", "India": "India",
"Indonesia": "Indonesia", "Iran": "Iran", "Iraq": "Iraq", "Ireland": "Ireland", "Israel": "Israel",
"Italy": "Italy", "Jamaica": "Jamaica", "Japan": "Japan", "Jordan": "Jordan", "Kazakhstan": "Kazakhstan",
"Kenya": "Kenya", "Kiribati": "Kiribati", "North Korea": "North Korea", "South Korea": "South Korea",
"Kosovo": "Kosovo", "Kuwait": "Kuwait", "Kyrgyzstan": "Kyrgyzstan", "Laos": "Laos", "Latvia": "Latvia",
"Lebanon": "Beirut", "Lesotho": "Maseru", "Liberia": "Monrovia", "Libya": "Tripoli", "Liechtenstein": "Vaduz",
"Lithuania": "Lithuania", "Luxembourg": "Luxembourg", "Macedonia": "Macedonia", "Madagascar": "Madagascar", "Malawi": "Malawi",
"Malaysia": "Malaysia", "Maldives": "Maldives", "Mali": "Mali", "Malta": "Malta", "Marshall Islands": "Marshall Islands",
"Mauritania": "Mauritania", "Mauritius": "Mauritius", "Mexico": "Mexico", "Federated States of Micronesia": "Federated States of Micronesia",
"Moldova": "Moldova", "Mongolia": "Mongolia", "Montenegro": "Montenegro", "Morocco": "Morocco",
"Mozambique": "Mozambique", "Myanmar": "Myanmar", "Namibia": "Namibia", "Nauru": "Nauru", "Nepal": "Nepal",
"Netherlands": "Netherlands", "New Zealand": "New Zealand", "Nicaragua": "Nicaragua", "Niger": "Niger", "Nigeria": "Nigeria",
"Norway": "Norway", "Oman": "Oman", "Pakistan": "Pakistan", "Panama": "Panama","Papua New Guinea": "Papua New Guinea", "Paraguay": "Paraguay",
"Peru": "Peru", "Philippines": "Philippines", "Poland": "Poland", "Portugal": "Portugal", "Qatar": "Qatar", "Romania": "Romania",
"Russia": "Moscow", "Rwanda": "Kigali", "Saint Kitts and Nevis": "Basseterre", "Saint Lucia": "Castries", 
"Saint Vincent and the Grenadines": "Saint Vincent and the Grenadines", "Samoa": "Samoa", "San Marino": "San Marino",
"Sao Tome and Principe": "Sao Tome", "Saudi Arabia": "Riyadh", "Senegal": "Dakar", "Serbia": "Belgrade", "Seychelles": "Victoria",
"Sierra Leone": "Sierra Leone", "Singapore": "Singapore", "Slovakia": "Slovakia", "Slovenia": "Slovenia", "Solomon Islands": "Solomon Islands",
"Somalia": "Somalia", "South Africa": "South Africa", "South Sudan": "South Sudan", "Spain": "Spain",
"Sri Lanka": "Sri Lanka", "Sudan": "Sudan", "Suriname": "Suriname", "Swaziland": "Swaziland",
"Sweden": "Sweden", "Switzerland": "Switzerland", "Syria": "Syria",  "Taiwan": "Taiwan", "Tajikistan": "Tajikistan",
"Tanzania": "Tanzania", "Thailand": "Thailand", "Togo": "Togo", "Tonga": "Tonga", "Trinidad and Tobago": "Trinidad and Tobago",
"Tunisia": "Tunisia", "Turkey": "Turkey", "Turkmenistan": "Turkmenistan", "Uganda": "Uganda",
"Ukraine": "Kyiv", "United Arab Emirates": "Abu Dhabi", "United Kingdom": "London", "United States of America": "United States of America",
"Uruguay": "Uruguay", "Uzbekistan": "Uzbekistan", "Vanuatu": "Vanuatu", "Vatican City": "Vatican City", "Venezuela": "Venezuela",
"Vietnam": "Vietnam", "Yemen": "Yemen", "Zambia": "Zambia", "Zimbabwe": "Zimbabwe"
}

COUNTRY_CHOICE = [(key, value) for key, value in COUNTRIES.items()]

BIRTH_CERTIFICATE = 'A'
NATIONAL_ID_CARD = 'B'
OLD_PASSPORT = 'C'
VOTER_ID_CARD = 'D'
DUAL_CITIZENSHIP_CARD = 'E'
NATURALIZATION_CARD = 'F'
REGISTRATION_CARD = 'G'

DOCUMENT_CHOICES = [
    (BIRTH_CERTIFICATE, 'Birth Certificate'),
    (NATIONAL_ID_CARD, 'National Identity Card'),
    (OLD_PASSPORT, 'Old Passport'),
    (VOTER_ID_CARD, 'Voter ID Card'),
    (DUAL_CITIZENSHIP_CARD, 'Dual Citizenship Card'),
    (NATURALIZATION_CARD, 'Naturalization Card'),
    (REGISTRATION_CARD, 'Registration Card'),
]

class Home(models.Model):
    pass

class About(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=True)
    content = models.TextField(max_length=5000, blank=False)
    image = models.ImageField(upload_to="about_images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=122, unique=True, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=155, blank=True)
    message = models.TextField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject


class ChangeContact(models.Model):
    office = models.CharField(max_length=1024)
    mobile = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.office
    

class Service(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    image = models.ImageField(upload_to="service_images", blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Applicant(models.Model):
    surname = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    other_name = models.CharField(max_length=100, blank=False)
    date_of_birth = models.DateField(blank=False)
    city_of_birth = models.CharField(max_length=100, blank=False)
    country_of_birth = models.CharField(max_length=100, blank=False)
    height = models.DecimalField(decimal_places=2, max_digits=5)
    eye_colour = models.CharField(max_length=20, blank=False)
    hair_colour = models.CharField(max_length=20, blank=False)
    nationality = models.CharField(max_length=100, default="Ghana")
    marital_status = models.CharField(max_length=2, choices=MARITAL_STATUS_CHOICES)
    profession = models.CharField(max_length=3, choices=PROFESSION_CHOICES)
    previous_profession = models.CharField(max_length=1, choices=CHOICE_SELECTION)
    national_ID_no = models.CharField(max_length=20)
    social_security_number = models.CharField(max_length=20, null=True)
    voters_ID_no = models.CharField(max_length=20, null=True)
    post_code = models.CharField(max_length=20)
    country_of_residence = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    street_number = models.CharField(max_length=10)
    digital_address = models.CharField(max_length=100)
    postal_address = models.CharField(max_length=100)
    telephone_no = models.CharField(max_length=20)
    email = models.EmailField()
    institution = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    period_from = models.DateField()
    period_to = models.DateField()
    Dual_citizen = models.CharField(max_length=10, choices=CHOICE_SELECTION)


class Father(models.Model):
    father_name = models.CharField(max_length=100)
    living = models.CharField(max_length=5, choices=CHOICE_SELECTION)
    nationality = models.CharField(max_length=50, default="Ghana")
    postal_address = models.CharField(max_length=100)
    residential_address = models.CharField(max_length=100)
    home_town = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)


class Mother(models.Model):
    mother_name = models.CharField(max_length=100)
    living = models.CharField(max_length=5, choices=CHOICE_SELECTION)
    nationality = models.CharField(max_length=50, default="Ghana")
    postal_address = models.CharField(max_length=100)
    residential_address = models.CharField(max_length=100)
    home_town = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

class GrandParent(models.Model):
    grand_parent_name = models.CharField(max_length=100, blank=False)
    living = models.CharField(max_length=5, choices=CHOICE_SELECTION)
    nationality = models.CharField(max_length=50, default="Ghana")
    postal_address = models.CharField(max_length=100)
    residential_address = models.CharField(max_length=100)
    home_town = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


class Guarantor(models.Model):
    full_name = models.CharField(max_length=100)
    residential_address = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255, blank=True)
    telephone_no = models.CharField(max_length=20)
    occupation = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()


class Declaration(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    telephone_no = models.CharField(max_length=20)
    date = models.DateField()


class PassportConsent(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    telephone_no = models.CharField(max_length=20)
    date = models.DateField()


class PassportApplication(models.Model):
    full_name = models.CharField(max_length=100)
    previous_passport_no = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()


class Document(models.Model):
    document_type = models.CharField(max_length=1, choices=DOCUMENT_CHOICES)
    number = models.CharField(max_length=50, blank=True)
    date_of_issue = models.DateField(null=True, blank=True)
    place_of_issue = models.CharField(max_length=100, blank=True)


class Witness(models.Model):
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    business_address = models.CharField(max_length=255)
    business_phone_no = models.CharField(max_length=20)
    residential_address = models.CharField(max_length=255)
    residential_phone_no = models.CharField(max_length=20)
    date = models.DateField()

    
class Passport(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    father = models.ForeignKey(Father, on_delete=models.CASCADE)
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)
    grand_parent = models.ForeignKey(GrandParent, on_delete=models.CASCADE)
    guarantor = models.ForeignKey(Guarantor, on_delete=models.CASCADE)
    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE)
    passportonsent = models.ForeignKey(PassportConsent, on_delete=models.CASCADE)
    passportapplication = models.ForeignKey(PassportApplication, on_delete=models.CASCADE)
    witness = models.ForeignKey(Witness, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.applicant.surname} {self.applicant.first_name}"


class PassportApplicantDetails(models.Model):
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE)
    applicant_ID = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    def applicant_name(self):
        return f"{self.passport.applicant.first_name} {self.passport.applicant.surname}"
    
    def father_name(self):
        return f"{self.passport.father.father_name}"
    
    def mother_name(self):
        return self.passport.mother.mother_name
    
    def guarantor_name(self):
        return self.passport.guarantor.full_name
    
    def witness_name(self):
        return self.passport.witness.full_name

    def __str__(self) -> str:
        return (f"{self.applicant_name()} {self.father_name()} {self.mother_name()} {self.guarantor_name()} {self.witness_name() - self.date_created.strftime('%Y-%m-%d %H:%M:%S')}")
    

class VisaProcess(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICE)
    type_of_visa = models.CharField(max_length=50, choices=VISA_TYPE_CHOICE)
    passport_number = models.CharField(max_length=50, blank=False, unique=True)
    passport_picture = models.ImageField(upload_to="Visa_process", blank=True)
    bank_statement = models.FileField(upload_to="Visa_process", blank=True)
    itinery = models.FileField(upload_to="Visa_process", blank=True)
    any_support_document = models.FileField(upload_to="Visa_process")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Country: {self.country} | type of Visa: {self.type_of_visa} | Passport Number: {self.passport_number}"


class HotelReservation(models.Model):
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICE)
    city = models.CharField(max_length=255, blank=False)
    adults = models.IntegerField(default=2)
    children = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.country


class SocialMediaHandle(models.Model):
    facebook = models.URLField(blank=False, unique=True)
    tiktok = models.URLField(blank=False, unique=True)
    instagram = models.URLField(blank=False, unique=True)
    twitter = models.URLField(blank=False, unique=True)
    youtube = models.URLField(blank=False, unique=True)


class EligibleCountry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ScholarshipBenefit(models.Model):
    description = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.description

class EligibleCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ScholarshipLink(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)
    host_country = models.CharField(max_length=100, unique=False, blank=False, choices=COUNTRY_CHOICE)
    eligible_countries = models.ManyToManyField(EligibleCountry)
    eligible_categories = models.ManyToManyField(EligibleCategory)
    benefits = models.ManyToManyField(ScholarshipBenefit)
    link = models.URLField()
    deadline = models.DateField()
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.host_country}: {self.deadline}"
    

class BirthCertificate(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    other_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(auto_now=False, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    place_of_birth = models.CharField(max_length=255, blank=False)
    father_name = models.CharField(max_length=255, blank=False)
    occupation = models.CharField(max_length=15, blank=False, unique=True)
    religion = models.CharField(max_length=255, blank=False)
    mother_name = models.CharField(max_length=255, blank=False)
    ghana_card_number = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Name of Applicant: {self.first_name} {self.surname}"


class BookFlight(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField()
    departure_date = models.DateField(auto_now=False)
    return_date = models.BooleanField(default=False)
    daparture_from= models.CharField(max_length=255, blank=False)
    destination = models.CharField(max_length=255, blank=False,)
    travellers = models.IntegerField(default=1)
    cabin_class = models.CharField(max_length=255, choices=CABIN_CLASS_CHOICES, default="Economy")
    travel_type = models.CharField(max_length=255, choices=SELECT_TYPE, default="One Way")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def set_return(self):
        if self.travel_type == "Return Trip":
            self.return_date = models.DateField(auto_now=False)
        
    def __str__(self) -> str:
        return self.full_name

class Package(models.Model):
    country_name = models.CharField(max_length=255, unique=False, blank=False, choices=COUNTRY_CHOICE)
    image = models.ImageField(upload_to="packages")
    number_of_people = models.IntegerField(default=5)
    number_of_days = models.IntegerField(default=7)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=500.00)
    short_content = models.CharField(max_length=255, blank=False, unique=True)
    full_content = models.TextField(max_length=2000, blank=True, unique=True)

    def __str__(self) -> str:
        return self.country_name

class PackageBook(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (self.package.country_name, self.full_name, self.contact)
    

class HolidayPlaces(models.Model):
    country = models.CharField(max_length=255, blank=False, unique=False, choices=COUNTRY_CHOICE)
    city = models.CharField(max_length=255, blank=False, unique=False)
    is_discount = models.BooleanField(default=False)
    discount_percent = models.DecimalField(max_digits=3, decimal_places=2, default=00.00)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}, {self.country} - {self.discount_display}"

class Destination(models.Model):
    image = models.ImageField(upload_to="destianation_images", blank=False, unique=True)
    country = models.CharField(max_length=120, blank=False, unique=False)
    content = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.country

class Guide(models.Model):
    full_name = models.CharField(max_length=120, blank=False, unique=True)
    image = models.ImageField(upload_to="guides_images", unique=True, blank=False)
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    destination = models.CharField(max_length=120, blank=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name
    

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email