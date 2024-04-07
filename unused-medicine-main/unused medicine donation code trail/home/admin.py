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
