from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User

# Create your views here.

def home(request):
    return render(request,"Register.html")


def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        # print(name)
        # print(phone)
        # print(email)
        # print(password)
        # print(cpassword)
        
        data=User.objects.filter(Email=email)
        if data:
            msg='Email already exist'
            return render(request,'Register.html',{'key':msg})
        elif password==cpassword:
                User.objects.create(Name=name,Phone=phone,Email=email,Password=password,Cpassword=cpassword)
                msg="Regastation succsessfully"
                #data = User.objects.all()
                return render(request,'Login.html')
        else:
                msg="password of cpassword not match"
                #return HttpResponse("successfully")
                return render(request,'Register.html',{'key':msg})
    else:
        msg="Welcome to registration page"
        return render(request,'Register.html',{'key':msg})

def login(req):
    if req.method=='POST':
        Emailllll=req.POST.get('email')
        Password=req.POST.get('password')
        print(Password)
        user=User.objects.filter(Email=Emailllll)
        if user:
            data=User.objects.get(Email=Emailllll)
            pass1=data.Password
            print(pass1)
            if pass1==Password:
                context={}
                context['name']=data.Name
                context['phone']=data.Phone
                context['email']=data.Email
                context['password']=data.Password
                msg="Login succsessfully"
                return render(req,"Dashboard.html",context)
            else:
                msg="Email or password not meatch"
                return render(req,"Login.html",{'key':msg})
        else:
            msg="Enter valid email"
            return render(req,"Login.html",{'key':msg})     
    else:
        msg="Welcome to login page"
        return render(req,"Login.html",{'key':msg})