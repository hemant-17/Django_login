from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import Sign
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def sign(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        #print(name)
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1= request.POST.get('password1','')
        password2= request.POST.get('password2','')
        #address=request.POST.get('address1','') + " "+ request.POST.get('address2','')
        #state=request.POST.get('state','')
        #city=request.POST.get('city','')
        #zip_code=request.POST.get('zip_code','')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME already registered ')
                #print('email taken ')
                return redirect('sign')
            #elif User.objects.filter(email=email).exits():
                #messages.info(request, ' phone number already registered ')
                #print('phone number used')
                #return redirect('sign')
            else:
                user = User.objects.create_user( first_name=first_name,last_name=last_name, username=username, email=email, password=password1 )
                #sign = Sign.objects.create_user( name=name,  email=email , phone=phone, password=password1, address=address, city=city, state=state, zip_code=zip_code )
                user.save()
                #print('user created')
                return redirect('login')
                #user = User.objects.create_user
        else:
            #print('password not matching')
            messages.info(request, 'Confirm password did not match ')
            return redirect('sign')

    return render(request,'trial/sign.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request,User)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'trial/login.html')

def logout(request):
    auth.logout(request)

    return redirect('/')
