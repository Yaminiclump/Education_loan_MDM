from django.contrib import admin

from mdm_services.models.city_model import City
# Register your models here.
from mdm_services.models.country_model import Country
from mdm_services.models.institute_model import Institute
from mdm_services.models.pincode_model import Pincode
from mdm_services.models.state_model import State

admin.site.register(Country)

admin.site.register(State)

admin.site.register(City)

admin.site.register(Institute)

admin.site.register(Pincode)