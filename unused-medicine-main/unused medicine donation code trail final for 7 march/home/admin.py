from django.contrib import admin
from .models import ngodetail, donordetail, medicine, newuser, Doctorinformation, uploadmedicine, ngologin, upload_medicine1, upload_equipment1, blood_donation1, buy1, equipment_buy1

# Register your models here.
admin.site.register(ngodetail)
admin.site.register(donordetail)
admin.site.register(medicine)
admin.site.register(newuser)
admin.site.register(Doctorinformation)
admin.site.register(uploadmedicine)
# admin.site.register(post)
# admin.site.register(postngo)
admin.site.register(ngologin)
admin.site.register(upload_medicine1)
admin.site.register(upload_equipment1)
admin.site.register(blood_donation1)
admin.site.register(buy1)
admin.site.register(equipment_buy1)
