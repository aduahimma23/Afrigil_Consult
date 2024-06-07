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
CABIN_CLASS_CHOICES = [
    (ECONOMY, 'Economy'),
    (BUSINESS, 'Business'),
    (FIRST_CLASS, 'First Class'),
]
ONE_WAY = "OW"
RETURN = "RT"
SELECT_TYPE = {
    (ONE_WAY, "One Way"),
    (RETURN, "Return Trip"),
}

COUNTRIES = {
"Afg": "Afghanistan", "Alb": "Albania", "Alg": "Algeria", "And": "Andorra", 
"Ang": "Angola", "Ant-b": "Antigua and Barbuda", "Arg": "Argentina",
"Armenia" : "Yerevan", "Australia" : "Canberra", "Austria" : "Vienna", "Azerbaijan" : "Baku",
"The Bahamas" : "Nassau", "Bahrain" : "Manama", "Bangladesh" : "Dhaka", "Barbados" : "Bridgetown",
"Belarus" : "Minsk", "Belgium" : "Brussels", "Belize" : "Belmopan", "Benin" : "Porto-Novo",
"Bhutan" : "Thimphu", "Bolivia" : "La Paz, Sucre", "Bosnia and Herzegovina" : "Sarajevo",
"Botswana" : "Gaborone", "Brazil" : "Brasilia", "Brunei" : "Bandar Seri Begawan", "Bulgaria" : "Sofia",
"Burkina Faso" : "Ouagadougou", "Burundi" : "Bujumbura", "Cambodia" : "Phnom Penh", "Cameroon" : "Yaounde",
"Canada" : "Ottawa", "Cape Verde" : "Praia", "Central African Republic" : "Bangui", "Chad" : "N’Djamena",
"Chile" : "Santiago", "China" : "Beijing", "Colombia" : "Bogota", "Comoros" : "Moroni", "Republic of the Congo": "Brazzaville",
"Democratic Republic of the Congo" : "Kinshasa", "Costa Rica" : "San Jose", "Cote d’Ivoire" : "Yamoussoukro",
"Croatia" : "Zagreb", "Cuba" : "Havana", "Cyprus" : "Nicosia", "Czech Republic" : "Prague", "Denmark" : "Copenhagen",
"Djibouti" : "Djibouti", "Dominica" : "Roseau", "Dominican Republic" : "Santo Domingo", "East Timor" : "Dili",
"Ecuador" : "Quito", "Egypt" : "Cairo", "El Salvador" : "San Salvador", "Equatorial Guinea" : "Malabo",
"Eritrea" : "Asmara", "Estonia" : "Tallinn", "Ethiopia" : "Addis Ababa", "Fiji" : "Suva", "Finland" : "Helsinki",
"France" : "Paris", "Gabon" : "Libreville", "The Gambia" : "Banjul", "Georgia" : "Tbilisi", "Germany" : "Berlin",
"Ghana" : "Accra", "Greece" : "Athens", "Grenada" : "Saint George’s", "Guatemala" : "Guatemala City",
"Guinea" : "Conakry", "Guinea-Bissau" : "Bissau", "Guyana" : "Georgetown", "Haiti" : "Port-au-Prince",
"Honduras" : "Tegucigalpa", "Hungary" : "Budapest", "Iceland" : "Reykjavik", "India" : "New Delhi",
"Indonesia" : "Jakarta", "Iran" : "Tehran", "Iraq" : "Baghdad", "Ireland" : "Dublin", "Israel" : "Jerusalem",
"Italy" : "Rome", "Jamaica" : "Kingston", "Japan" : "Tokyo", "Jordan" : "Amman", "Kazakhstan" : "Astana",
"Kenya" : "Nairobi", "Kiribati" : "Tarawa Atoll", "North Korea" : "Pyongyang", "South Korea" : "Seoul",
"Kosovo" : "Pristina", "Kuwait" : "Kuwait City", "Kyrgyzstan" : "Bishkek", "Laos" : "Vientiane", "Latvia" : "Riga",
"Lebanon" : "Beirut", "Lesotho" : "Maseru", "Liberia" : "Monrovia", "Libya" : "Tripoli", "Liechtenstein" : "Vaduz",
"Lithuania" : "Vilnius", "Luxembourg" : "Luxembourg", "Macedonia" : "Skopje", "Madagascar" : "Antananarivo", "Malawi" : "Lilongwe",
"Malaysia" : "Kuala Lumpur", "Maldives" : "Male", "Mali" : "Bamako", "Malta" : "Valletta", "Marshall Islands" : "Majuro",
"Mauritania" : "Nouakchott", "Mauritius" : "Port Louis", "Mexico" : "Mexico City", "Federated States of Micronesia" : "Palikir",
"Moldova" : "Chisinau", "Monaco" : "Monaco", "Mongolia" : "Ulaanbaatar", "Montenegro" : "Podgorica", "Morocco" : "Rabat",
"Mozambique" : "Maputo", "Myanmar" : "Naypyidaw", "Namibia" : "Windhoek", "Nauru" : "Yaren District", "Nepal" : "Kathmandu",
"Netherlands" : "Amsterdam", "New Zealand" : "Wellington", "Nicaragua" : "Managua", "Niger" : "Niamey", "Nigeria" : "Abuja",
"Norway" : "Oslo", "Oman" : "Muscat", "Pakistan" : "Islamabad", "Palau" : "Melekeok", "Panama" : "Panama City",
"Papua New Guinea" : "Port Moresby", "Paraguay" : "Asuncion", "Peru" : "Lima", "Philippines" : "Manila", "Poland" : "Warsaw",
"Portugal" : "Lisbon", "Qatar" : "Doha", "Romania" : "Bucharest", "Russia" : "Moscow", "Rwanda" : "Kigali", "Saint Kitts and Nevis" : "Basseterre",
"Saint Lucia" : "Castries", "Saint Vincent and the Grenadines" : "Kingstown", "Samoa" : "Apia", "San Marino" : "San Marino",
"Sao Tome and Principe" : "Sao Tome", "Saudi Arabia" : "Riyadh", "Senegal" : "Dakar", "Serbia" : "Belgrade", "Seychelles" : "Victoria",
"Sierra Leone" : "Freetown", "Singapore" : "Singapore", "Slovakia" : "Bratislava", "Slovenia" : "Ljubljana", "Solomon Islands" : "Honiara",
"Somalia" : "Mogadishu", "South Africa" : "Pretoria, Cape Town, Bloemfontein", "South Sudan" : "Juba", "Spain" : "Madrid",
"Sri Lanka" : "Colombo, Sri Jayewardenepura Kotte", "Sudan" : "Khartoum", "Suriname" : "Paramaribo", "Swaziland" : "Mbabane",
"Sweden" : "Stockholm", "Switzerland" : "Bern", "Syria" : "Damascus",  "Taiwan" : "Taipei", "Tajikistan" : "Dushanbe",
"Tanzania" : "Dodoma", "Thailand" : "Bangkok", "Togo" : "Lome", "Tonga" : "Nuku’alofa", "Trinidad and Tobago" : "Port-of-Spain",
"Tunisia" : "Tunis", "Turkey" : "Ankara", "Turkmenistan" : "Ashgabat", "Tuvalu" : "Funafuti", "Uganda" : "Kampala",
"Ukraine" : "Kyiv", "United Arab Emirates" : "Abu Dhabi", "United Kingdom" : "London", "United States of America" : "Washington D.C.",
"Uruguay" : "Montevideo", "Uzbekistan" : "Tashkent", "Vanuatu" : "Port-Vila", "Vatican City" : "Vatican City", "Venezuela" : "Caracas",
"Vietnam" : "Hanoi", "Yemen" : "Sanaa", "Zambia" : "Lusaka", "Zimbabwe" : "Harare"
}

COUNTRY_CHOICE = [(key, value) for key, value in COUNTRIES.items()]

class Home(models.Model):
    pass

class About(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    content = models.TextField(max_length=5000, blank=False)
    image = models.ImageField(upload_to="about_images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=122, unique=True, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=155, blank=True)
    message = models.TextField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name


class ChangeContact(models.Model):
    office = models.CharField(max_length=1024)
    mobile = models.IntegerField()
    email = models.EmailField()

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
    maiden_name = models.CharField(max_length=100, blank=False)
    date_of_birth = models.DateField()
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
    social_security_number = models.CharField(max_length=20)
    voters_ID_no = models.CharField(max_length=20)
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
    signature = models.ImageField(upload_to='signatures/')
    date = models.DateField()


class Declaration(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    telephone_no = models.CharField(max_length=20)
    signature = models.ImageField(upload_to='declarations/')
    date = models.DateField()


class PassportConsent(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    telephone_no = models.CharField(max_length=20)
    signature = models.ImageField(upload_to='passport_consents/')
    date = models.DateField()


class PassportApplication(models.Model):
    full_name = models.CharField(max_length=100)
    previous_passport_no = models.CharField(max_length=20, blank=True, null=True)
    signature = models.ImageField(upload_to='passport_applications/')
    date = models.DateField()


class Document(models.Model):
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
    signature = models.ImageField(upload_to='witness_signatures/')
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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Country: {self.country} | type of Visa: {self.type_of_visa} | Passport Number: {self.passport_number}"


class HotelReservation(models.Model):
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICE)
    city = models.CharField(max_length=255, blank=False)
    check_in = models.DateField(auto_now=True, blank=False)
    check_out = models.DateField(auto_now=False, blank=False,)
    adults = models.IntegerField(default=2)
    children = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.country


class SocialMediaHandles(models.Model):
    facebook = models.URLField(blank=False, unique=True)
    tiktok = models.URLField(blank=False, unique=True)
    instagram = models.URLField(blank=False, unique=True)
    twitter = models.URLField(blank=False, unique=True)
    youtube = models.URLField(blank=False, unique=True)


class ScholarshipLinks(models.Model):
    institute_name = models.CharField(max_length=255, unique=True, null=False)
    country = models.CharField(max_length=100, unique=False, blank=False, choices=COUNTRY_CHOICE)
    state = models.CharField(max_length=100, unique=False, null=False)
    organization = models.CharField(max_length=100, null=False, unique=False)
    image = models.ImageField(upload_to="scholarship_images")
    link = models.URLField()
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.institute_name
    

class BirthCertificate(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    other_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(auto_now=False, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    place_of_birth = models.CharField(max_length=255, blank=False)
    distirct = models.CharField(max_length=100, blank=False)
    region = models.CharField(max_length=255, blank=False)
    parent_name = models.CharField(max_length=255, blank=False)
    contact = models.CharField(max_length=15, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


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
        return self.name

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

    @property
    def discount_display(self):
        if self.is_discount:
            discount_amount = self.cost * (self.discount_percent / 100)
            discounted_cost = self.cost - discount_amount
            return f"Discount: {self.discount_percent}% | Discounted Cost: {discounted_cost}"
        else:
            return "Discount: 0%"

    def __str__(self):
        return f"{self.city}, {self.country} - {self.discount_display}"


class Guides(models.Model):
    full_name = models.CharField(max_length=120, blank=False, unique=True)
    image = models.ImageField(upload_to="guides_images", unique=True, blank=False)
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    destination = models.CharField(max_length=120, blank=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name