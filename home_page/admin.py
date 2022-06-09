import imp
from django.contrib import admin
from home_page.models import Registration_models, Blood_donate_model, Order_blood_model, Received_unit_model

# Register your models here.
admin.site.register(Registration_models)
admin.site.register(Blood_donate_model)
admin.site.register(Order_blood_model)
admin.site.register(Received_unit_model)
