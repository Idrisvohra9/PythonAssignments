from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from Home.models import Services
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'variable1':"Sharma Tyres for a smooth experience.",
        'variable2':"For a safe life",  
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")

def services(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pname = request.POST.get('pname')
        pay = request.POST.get('pay')
        services = Services(name=name, email=email, phone=phone, address=address,pname=pname,pay=pay,date=datetime.today())
        services.save()
        messages.success(request, 'Your message has been sent!')
        
    return render(request,'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")

def blog(request):
    return render(request,'blog.html')

def shop(request):
    return render(request,'shop.html')
