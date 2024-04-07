from django.shortcuts import render, HttpResponse, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .forms import CreateUserForm, CreatengoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decoraters import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .models import doctordetail, ngodetail, donordetail, medicine
from datetime import date
from django.contrib.auth.models import User
from django.contrib import auth
from home  import views
from django import forms
from django.shortcuts import render, redirect
from .forms import MedicineForm
from .models import buy1, equipment_buy1, newuser,Doctorinformation, ngologin,  upload_equipment1, upload_medicine1, blood_donation1
from .models import upload_medicine1

# username- admin password- admin@1234   <------  Superuser
# Create your views here.
@unauthenticated_user
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")
    
@unauthenticated_user
def registerdonor(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Check if the 'donor' group exists, and create it if it doesn't
            group_name = 'donor'
            group, created = Group.objects.get_or_create(name=group_name)

            # Add the user to the 'donor' group
            user.groups.add(group)

            # Create donor details
            donordetail.objects.create(user=user)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
       
    context = {'form': form}
    return render(request, 'registerdonor.html', context)




@unauthenticated_user
def registerseller(request):
    form = CreateUserForm()
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # this is used for getting the username in views 
            username = form.cleaned_data.get('username')
            
            # create group
            
            group=Group.objects.get(name='donor')
            user.groups.add(group)
            donordetail.objects.create(
                user=user
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registerseller.html', context)

def Registerdoctor(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='doctor')
            user.groups.add(group)

            doctordetail.objects.create(user=user)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registerdoctor.html', context)

@unauthenticated_user
def registerngo(request):
    form = CreatengoForm()
    if(request.method == 'POST'):
        form = CreatengoForm(request.POST)
        if form.is_valid():
            user = form.save()
            # this is used for getting the username in views 
            username = form.cleaned_data.get('username')
            group=Group.objects.get(name='ngo')
            user.groups.add(group)
            ngodetail.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registerngo.html', context)
    # return HttpResponse("this is register page")

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/admindashboard')
        
        else:
            
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)
    # return HttpResponse("this is login page")
def logoutuser(request):
    logout(request)
    return redirect('login')
    # return HttpResponse("this is logout page")
@unauthenticated_user
def aboutus(request):
    return render(request, 'about-us.html')
    # return HttpResponse("this is logout page")

@unauthenticated_user
def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['ngo'])
def detailsngo(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        city = request.POST['city'] 
        state = request.POST['state'] 
        address = request.POST['address'] 
        phone = request.POST['phone'] 
        authority = request.POST['authority'] 
        registrationnum = request.POST.get('registrationnum')
        # print(name, city, state)

        details=ngodetail(name=name, city=city, state=state, address=address, phone=phone, authority=authority, registrationnum=registrationnum)

        details.save()
        return render(request, 'NGOdashboard1.html')



    return render(request, 'detailsngo.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def detailsdonor(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        city = request.POST['city'] 
        state = request.POST['state'] 
        address = request.POST['address'] 
        phone = request.POST['phone'] 

        details=donordetail(name=name, city=city, state=state, address=address, phone=phone)

        details.save()
        return render(request, 'donorDashboard1.html')

    return render(request, 'detailsdonor.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@admin_only
def adminaction(request):
    return render(request, 'adminaction.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@admin_only
def admindashboard(request):
    donors=donordetail.objects.all()
    ngos=ngodetail.objects.all()

    total_donors= donors.count()
    total_ngo= ngos.count()
    context={'donors':donors, 'ngos':ngos, 'total_donors':total_donors, 'total_ngo':total_ngo}
    return render(request, 'admindashboard1.html', context)
    # return HttpResponse("this is logout page")


@login_required(login_url='login')
@allowed_users(allowed_roles=['ngo'])
def ngodashboard(request):
    donors=donordetail.objects.all()
    ngos=ngodetail.objects.all()

    total_donors= donors.count()
    sum=total_ngo +total_donors
    context={'total_donors':total_donors, 'total_ngo':total_ngo, 'sum':sum}
    # posts=postngo.objects.all()
    # if request.method=='POST':
    #     desc = request.POST['desc']
    #     user = request.user.username 
    #     print(user)
    #     # post.objects.create(
    #     #     user=user
    #     # )
    #     c=postngo(desc=desc)
    #     c.save()

    #     posts=postngo.objects.all()

    #     no_of_ngo=ngodetail.objects.all()
    #     total_ngo=no_of_ngo.count()

    #     # name=donordetail.object

    # context={'posts':posts}
        


    return render(request, 'NGOdashboard1.html', context)
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def donordashboard(request):
    donors=donordetail.objects.all()
    ngos=ngodetail.objects.all()

    total_donors= donors.count()
    total_ngo= ngos.count()
    sum=total_ngo+total_donors
    context={'total_donors':total_donors, 'total_ngo':total_ngo, 'sum':sum}
    # posts=post.objects.all()
    # if request.method=='POST':
    #     desc = request.POST['desc']
    #     user = request.user.username 
    #     print(user)
    #     # post.objects.create(
    #     #     user=user
    #     # )
    #     c=post(desc=desc)
    #     c.save()

    #     posts=post.objects.all()

    #     no_of_ngo=ngodetail.objects.all()
    #     total_ngo=no_of_ngo.count()

    #     # name=donordetail.object

    # context={'posts':posts}
        

    return render(request, 'donorDashboard1.html', context)
    # return HttpResponse("this is logout page")


@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def donorprofile(request):
    donors=donordetail.objects.all()
    context={'donors':donors}

    return render(request, 'donorprofile.html', context)
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['ngo'])
def ngoprofile(request):

    return render(request, 'ngoprofile.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def medicinedonation(request):
    if request.method == 'POST':
        medicinename = request.POST['medicinename'] 
        companyname = request.POST['companyname'] 
        manufacturing = request.POST['manufacturing'] 
        expiry = request.POST['expiry'] 
        tablets = request.POST['tablets'] 

        details=medicine(medicinename=medicinename, companyname=companyname, manufacturing=manufacturing, expiry=expiry, tablets=tablets)

        details.save()
        return render(request, 'donorDashboard1.html')
    return render(request, 'MedicineDonation.html')
    # return HttpResponse("this is logout page")



def search_ngos(request):
    return render(request, 'thankyou.html' )

# views.py


# from django.shortcuts import render

# from django.http import  JsonResponse
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib import messages
# # Create your views here.
# from .models import newuser,Doctorinformation,uploadmedicine
# Create your views here.

def navbar(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('user_home')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
    return render(request, 'user_login.html')

def user_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('registration')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('user_login')
    else:
        return render(request, 'user_registration.html')

def user_home(request):
    return render(request, 'userhome.html')



def user_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')


def admin_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('admin_home')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request, 'admin_login.html')

def admin_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('admin_registration')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('admin_login')
    else:
        return render(request, 'admin_registration.html')

def admin_home(request):
    return render(request, 'admin_home.html')


def admin_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')



def doctor_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=Doctorinformation.objects.get(dname=request.POST['dname'], pass1=request.POST['pass1'])
            print("dname=",Userdetailes)
            request.session['dname']=Userdetailes.dname
            messages.success(request,"successfully login")
            return redirect('doctor_home')
        except Doctorinformation.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request, 'doctor_login.html')

def doctor_registration(request):
    if request.method == 'POST':
        
        dname=request.POST['dname']
        address=request.POST['address']
        email=request.POST['email']
        mobileno=request.POST['mobileno']
        qual=request.POST['qual']
        exe=request.POST['exe']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if Doctorinformation.objects.filter(dname=dname).exists():
            messages.warning(request,'Username is already exists')
            return redirect('doctor_registration')
        else:
            Doctorinformation(dname=dname, address=address, email=email, mobileno=mobileno, qual=qual,exe=exe,pass1=pass1).save()
            messages.success(request, 'The new user '+request.POST['dname']+ " IS saved successfully..!")
            return redirect('doctor_login')
    else:
        return render(request, 'doctor_registration.html')

def doctor_home(request):
    return render(request, 'doctor_home.html')


def doctor_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')

def ngo_login(request):
    return render(request, 'ngo_login.html')

def ngo_registration(request):
    return render(request, 'ngo_registration.html')



def upload_medicine(request):
    if request.method == 'POST':
        tmedicine=request.POST['tmedicine']
        mname=request.POST['mname']
        cname=request.POST['cname']
        mdate=request.POST['mdate']
        exdate=request.POST['exdate']
        ml=request.POST['ml']
        medicine=request.POST['medicine']
        quantity=request.POST['quantity']
        uname=request.POST['uname']
        address=request.POST['address']
        phone=request.POST['phone']
        email=request.POST['email']
        image=request.FILES['image']
        image2=request.FILES['image2']
        uploadmedicine(tmedicine=tmedicine, mname=mname, cname=cname, mdate=mdate, exdate=exdate, ml=ml, medicine=medicine, quantity=quantity, uname=uname,address=address, phone=phone, email=email, image=image, image2=image2).save()
        messages.success(request, 'The new user '+request.POST['uname']+ " IS saved successfully..!")
        return redirect('donordashboard')
    else:
        return render(request, 'UploadMedicine.html')
    
def navbar(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('user_home')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
    return render(request, 'user_login.html')

def user_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('user_login')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('user_login')
    else:
        return render(request, 'user_registration.html')

def user_home(request):
    return render(request, 'userhome.html')

def buy(request):
    if request.method == 'POST':
     medicine_name=request.POST.get('medicine_name')
     Manufacturing_date=request.POST.get('Manufacturing_date')
     expiry_date=request.POST.get('expiry_date')
     name=request.POST.get('name')
     mobile_no=request.POST.get('mobile_no')
     email=request.POST.get('email')
     address=request.POST.get('address')
     buy1(medicine_name=medicine_name,Manufacturing_date=Manufacturing_date,expiry_date=expiry_date,name=name,mobile_no=mobile_no,email=email,address=address).save()
     return redirect('buy')
    else:
        return render(request, 'buy.html')

def cipla_details(request):
    # messages.success(request,"Generic Name:Cipla Paracetamol,Description:Paracip-500 Tablet 10's belongs to the group of medicines called analgesics (pain killers), and antipyretics (fever-reducing agents) used to reduce fever and treat mild to moderate pain. Also, it is used to relieve headache, migraine, toothache, period pain, back pain, muscle pain and rheumatic pains,Strength: 500mg,Manufacturer:Cipla,Shelf life: 24 Months")
    return render(request, 'cipla_details.html')

def fever_details(request):
    return render(request,'fever_details.html')

def paracetamol(request):
    return render(request,'paracetamol.html')

def para500mg(request):
    return render(request,'para500mg.html')

def dolo(request):
    return render(request,'dolo.html')

def midodrine(request):
    return render(request,'midodrine.html')

def vnydaqel(request):
    return render(request,'vnydaqel.html')

def carvedilol(request):
    return render(request,'carvedilol.html')


def doctorinfo(request):
    return render(request,'doctorinfo.html')


def docinfo(request):
    return render(request,'docinfo.html')




def user_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')


def admin_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('admin_home')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request, 'admin_login.html')

def admin_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('admin_registration')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('admin_login')
    else:
        return render(request, 'admin_registration.html')

def admin_home(request):
    return render(request, 'admin_home.html')



def admin_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')

def NGO(request):
    return render(request, 'NGO.html')



def doctor_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=Doctorinformation.objects.get(dname=request.POST['dname'], pass1=request.POST['pass1'])
            print("dname=",Userdetailes)
            request.session['dname']=Userdetailes.dname
            messages.success(request,"successfully login")
            return redirect('doctor_home')
        except Doctorinformation.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request, 'doctor_login.html')

def doctor_registration(request):
    if request.method == 'POST':
        
        dname=request.POST['dname']
        address=request.POST['address']
        email=request.POST['email']
        mobileno=request.POST['mobileno']
        qual=request.POST['qual']
        exe=request.POST['exe']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if Doctorinformation.objects.filter(dname=dname).exists():
            messages.warning(request,'Username is already exists')
            return redirect('doctor_registration')
        else:
            Doctorinformation(dname=dname, address=address, email=email, mobileno=mobileno, qual=qual,exe=exe,pass1=pass1).save()
            messages.success(request, 'The new user '+request.POST['dname']+ " IS saved successfully..!")
            return redirect('doctor_login')
    else:
        return render(request, 'doctor_registration.html')

def doctor_home(request):
    return render(request, 'doctor_home.html')

def needy(request):
    return render(request, 'needy.html')

def blood_donation(request):
    if request.method == 'POST':
      name=request.POST.get('name')
      mobile_no=request.POST.get('mobile_no')
      email=request.POST.get('email')
      blood_group=request.POST.get('blood_group')
      age=request.POST.get('age')
      weight=request.POST.get('weight')
      any_health_issue=request.POST.get('any_health_issue')
      blood_donation1(name=name,mobile_no=mobile_no,email=email,blood_group=blood_group,age=age,weight=weight,any_health_issue=any_health_issue).save()
      return redirect('blood_donation')
    else:
        return render(request, 'blood_donation.html')


def doctor_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')

def ngo_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=ngologin.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('NGO')
        except ngologin.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
   
    return render(request, 'ngo_login.html')

def ngo_registration(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        pass1=request.POST.get('pass1')
        fname=request.POST.get('fname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        ngo_start_date=request.POST.get('ngo_start_date')
        
        ngologin(Username=Username,pass1=pass1,fname=fname,address=address,email=email,mobileno=mobileno,ngo_start_date=ngo_start_date).save()
        messages.success(request, 'The data in databse' " IS saved successfully..!")
        return redirect('ngo_login')
    else:

     return render(request, 'ngo_registration.html')


def ngo_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('navbar')

def upload_unused_medicine_details(request):
    return render(request, 'upload_unused_medicine_details.html')

def upload_medicine(request):
    if request.method == 'POST':
         name=request.POST.get('name')
         mobile_no=request.POST.get('mobile_no')
         email=request.POST.get('email')
         expiry_date=request.POST.get('expiry_date')
         image=request.FILES.get('image')
         medicine_name=request.POST.get('medicine_name')
         quantity=request.POST.get('quantity')
         description=request.POST.get('description')
         Manufacturing_date=request.POST.get('Manufacturing_date')
         upload_medicine1(name=name,mobile_no=mobile_no,email=email,expiry_date=expiry_date,image=image,medicine_name=medicine_name,quantity=quantity,description=description,Manufacturing_date=Manufacturing_date).save()
         messages.success(request, 'The data in databse' " IS saved successfully..!")
         return redirect('upload_medicine')
    else:

     return render(request, 'upload_medicine.html')

def showuser(request):
    medicines = upload_medicine1.objects.all()
    return render(request, 'showuser.html', {'medicines': medicines})


def upload_equipment(request):
     if request.method == 'POST':
      name=request.POST.get('name')
      mobile_no=request.POST.get('mobile_no')
      email=request.POST.get('email')
      equipment_name=request.POST.get('equipment_name')
      image=request.FILES.get('image')
      quantity=request.POST.get('quantity')
      description=request.POST.get('description')
      upload_equipment1(name=name,mobile_no=mobile_no,email=email,equipment_name=equipment_name,image=image,quantity=quantity,description=description).save()
      messages.success(request, 'The data in databse' " IS saved successfully..!")
      return redirect('upload_equipment')
     else:
      return render(request, 'upload_equipment.html')
     
def search(request):
    query=request.GET['query']
    form=upload_medicine1.objects.filter(medicine_name__icontains=query)
    return render (request, 'search.html',{'forms':form})


def search_equiments(request):
    query=request.GET['query']
    form=upload_equipment1.objects.filter(equipment_name__icontains=query)

    return render(request,'search1.html',{'forms':form})




def medical_verify(request):
    return render(request,'medical_verify.html')

def equipment(request):
    return render(request,'equipment.html')

def equipment_buy(request):
     if request.method == 'POST':
         Equipment_name=request.POST.get('Equipment_name')
         name=request.POST.get('name')
         mobile_no=request.POST.get('mobile_no')
         email=request.POST.get('email')
         address=request.POST.get('address')
         equipment_buy1(Equipment_name=Equipment_name,name=name,mobile_no=mobile_no,email=email,address=address).save()
         return redirect('equipment_buy')
     else:

         return render(request, 'equipment_buy.html')




def viewsearch(request):
    form = upload_medicine1.objects.all()
    # upload_medicine1 = {'allPosts': upload_medicine1}
    print('MyOutput',form)
    return render(request,'viewsearch.html',{'params':form})

def showuser1(request):
    equipment = upload_equipment1.objects.all()
    return render(request, 'showuser1.html', {'equipment': equipment})

     


def medicine_verifications(request):
    medicines = upload_medicine1.objects.all()
    return render(request, 'medical_verifications.html', {'medicines': medicines})


def show_user(request):
    medicines = newuser.objects.all()
    return render(request, 'show_user.html', {'medicines': medicines})

def show_doctor(request):
    medicines = Doctorinformation.objects.all()
    return render(request, 'show_doctor.html', {'medicines': medicines})