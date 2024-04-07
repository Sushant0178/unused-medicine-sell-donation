from django.contrib import admin
from .models import ngodetail, donordetail, medicine
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ngodetail)
admin.site.register(donordetail)
admin.site.register(medicine)
# Register your models here.
admin.site.register(newuser)
admin.site.register(Doctorinformation)
admin.site.register(uploadmedicine)
# admin.site.register(post)
# admin.site.register(postngo)
# admin.site.register(Doctorinformation)
admin.site.register(ngologin)
admin.site.register(upload_medicine1)
admin.site.register(upload_equipment1)
admin.site.register(blood_donation1)
admin.site.register(buy1)
admin.site.register(equipment_buy1)