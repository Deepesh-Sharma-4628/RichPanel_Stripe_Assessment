from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Plans,current_plan
import stripe
# Create your views here.
@login_required(login_url='login')
def Monthly(request):
    plan=Plans.objects.all()
    print(plan[0])
    return render (request,'monthly.html',{'plan':plan[0]})
def Yearly(request):
    plan=Plans.objects.all()
    return render (request,'yearly.html',{'plan':plan[1]})

@login_required(login_url='signup')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('monthly')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def mobilem(request):
    cp=current_plan.objects.all()
    cp.delete()
    plan=Plans.objects.all()
    
    en=current_plan(Plan_Name="Mobile",price=plan[0].Mobile)
    en.save()
    return render (request,'mobilem.html',{'plan':plan[0]})

def mobiley(request):
    cp=current_plan.objects.all()
    cp.delete()
    plan=Plans.objects.all()
    
    en=current_plan(Plan_Name="Mobile",price=plan[1].Mobile)
    en.save()
    return render (request,'mobiley.html',{'plan':plan[1]})

def basicm(request):
    cp=current_plan.objects.all()
    cp.delete()
    plan=Plans.objects.all()
   
    en=current_plan(Plan_Name="Basic",price=plan[0].Basic)
    en.save()
    return render (request,'basicm.html',{'plan':plan[0]})

def basicy(request):
    cp=current_plan.objects.all()
    cp.delete()
    plan=Plans.objects.all()
   
    en=current_plan(Plan_Name="Basic",price=plan[1].Basic)
    en.save()
    return render (request,'basicy.html',{'plan':plan[1]})

def standardm(request):
    cp=current_plan.objects.all()
    cp.delete()
    plan=Plans.objects.all()
    
    en=current_plan(Plan_Name="Standard",price=plan[0].Standard)
    en.save()
    return render (request,'standardm.html',{'plan':plan[0]})

def standardy(request):
    cp=current_plan.objects.all()
    cp.delete()
    plan=Plans.objects.all()
    
    en=current_plan(Plan_Name="Standard",price=plan[1].Standard)
    en.save()
    return render (request,'standardy.html',{'plan':plan[1]})

def premiumm(request):
    cp=current_plan.objects.all()
    cp.delete()
    plan=Plans.objects.all()
    
    en=current_plan(Plan_Name="Premium",price=plan[0].Premium)
    en.save()
    return render (request,'premiumm.html',{'plan':plan[0]})

def premiumy(request):
    cp=current_plan.objects.all()
    cp.delete()
    plan=Plans.objects.all()
    
    en=current_plan(Plan_Name="Premium",price=plan[1].Premium)
    en.save()
    return render (request,'premiumy.html',{'plan':plan[1]})

stripe.api_key='sk_test_51NbkLUSDGqB0Mn28uwrCbXcnhxeM1Ns3kAxpCLNYg7Gsb6GOqCwPhBLfjtSjzWMupZYcGgg9Sx8h1nWPsT2eGhPb00ZrsmSVDx'
def checkout(request):
    cp=current_plan.objects.all()
    if request.method=="POST":
        name=request.POST.get('')
    session = stripe.checkout.Session.create(
     payment_method_types=['card'],
      line_items= [{
        'price_data':{
            'currency':'inr',
            'product_data':{
                'name':cp[0].Plan_Name,
            },
            'unit_amount':cp[0].price*100,
        },
        'quantity':1,
      }],
      mode='payment',
      success_url='http://127.0.0.1:8000/success',
      cancel_url='http://127.0.0.1:8000/cancel',
    )
    return redirect (session.url, 303)


def success(request):
    cp=current_plan.objects.all()
    d=current_plan.objects.all()
    en=current_plan(Plan_Name=cp[0].Plan_Name,price=cp[0].price,subscription='Active')
    en.save()
    d[0].delete()
    return render (request,'success.html',{'cp':cp[0]})
@login_required(login_url='login')
def cancel(request):
    cp=current_plan.objects.all()
    d=current_plan.objects.all()
    en=current_plan(Plan_Name=cp[0].Plan_Name,price=cp[0].price,subscription='Cancelled')
    en.save()
    d[1].delete()
    return render (request,'cancel.html',{'cp':cp[0]})