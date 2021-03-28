from django.shortcuts import render,redirect
from . import models
# from django_component import Library, Component
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    
def payment(request):
   
    if request.method=="POST":
        ammount=request.POST['ammount']
        Id=request.POST['id']
        Dname=request.POST['Dname']
        test = models.organization.objects.get(id=Id)
        if (test):
            # a=test.cammount
            models.organization.objects.filter(id=Id).update(cammount=ammount,Dname=Dname)
            return redirect('/')
        else:
            messages.info(request,test.id)
            return render(request,'paymentgateway.html')
    else:

        return render(request,'paymentgateway.html')  

def payment2(request,username):
    return render(request,'payment2.html')  

def dashb(request):
    if request.method=="POST":
        Id=request.POST['id']
        at= models.organization.objects.filter(id=Id)
        return render(request,'dashb.html')    
    return render(request,'dashb.html')

def donator(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        at = models.organization.objects.filter(username=username,password=password)
        test= models.organization.objects.all()
        if (at):
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return (redirect('dashb'))
        else:
            messages.info(request,"Username or Password wrong ")
            return redirect('donator')  
    else:
        return render(request,'login.html')

def info(request):
    # component = Component.objects.get(id=component_id)
    tests = models.organization.objects.all()
    context = {'tests':tests}
    print= tests
    return render(request,'info.html',context)    

def register(request):

    if request.method=="POST":
        user=request.POST['username']
        emai=request.POST['email']
        passwor1=request.POST['password1']
        passwor2=request.POST['password2']
        de=request.POST['des']
        # nu=request.POST['num']
        image=request.POST['images']
        if(passwor1==passwor2):
            if(models.organization.objects.filter(username=user)):
                messages.info(request,'Username Taken')
                return redirect('register')

            elif(models.organization.objects.filter(email=emai)):
                messages.info(request,'URL Taken')
                return redirect('register')
            # elif(models.organization.objects.filter(number=nu)):
            #     messages.info(request,'Number already taken')  
            #     return redirect('donator')        
            else:
                ins=models.organization(username=user,email=emai,password=passwor1,des=de,img=image)
                ins.save()
                return redirect('donator')
        else:
            messages.info(request,'Password worng')
            return redirect('register')        
    else:   
        return render(request,'register.html')  


# def home_page(request):
#     return render(request,'home_page.html')
      