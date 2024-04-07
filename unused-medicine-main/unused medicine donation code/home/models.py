from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime
# Create your models here.
class ngodetail(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	authority = models.CharField(max_length=200, null=True)
	registrationnum = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class donordetail(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class doctordetail(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name




class medicine(models.Model):
	medicinename = models.CharField(max_length=200, null=True)
	companyname = models.CharField(max_length=200, null=True)
	manufacturing =models.DateField(default='2020-01-01')
	expiry = models.DateField(default='2025-01-01')
	tablets = models.CharField(max_length=200, null=True)
	

	def __str__(self):
		return self.medicinename



# class post(models.Model):
# 	desc = models.CharField(max_length=200, null=True)
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	timestamp=models.DateTimeField(auto_now_add=True, blank=True)
# 	def __str__(self):
# 		return self.desc[:7]


# class postngo(models.Model):
# 	desc = models.CharField(max_length=200, null=True)
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	timestamp=models.DateTimeField(auto_now_add=True, blank=True)
# 	def __str__(self):
# 		return self.desc[:7]






# Create your models here.
class newuser(models.Model):
    Username=models.CharField(max_length=80)
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    email=models.EmailField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)

    def __str__(self):
        
	    return self.Username
   

class Doctorinformation(models.Model):
    dname=models.CharField(max_length=80)
    address=models.CharField(max_length=89)
    
    email=models.EmailField(max_length=90)
    mobileno=models.CharField(max_length=90)
    qual=models.CharField(max_length=90)
    exe=models.CharField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)


class uploadmedicine(models.Model):
    tmedicine=models.CharField(max_length=80)
    mname=models.CharField(max_length=89)
    
    cname=models.CharField(max_length=90)
    mdate=models.CharField(max_length=90)
    exdate=models.CharField(max_length=90)
    ml=models.CharField(max_length=90)
    medicine=models.CharField(max_length=90)
    quantity=models.CharField(max_length=90)
    uname=models.CharField(max_length=90)
    address=models.CharField(max_length=90)
    phone=models.CharField(max_length=90)
    email=models.EmailField(max_length=90)
    image=models.ImageField(upload_to='images',default="")  
    image2=models.ImageField(upload_to='images',default="")  
    
