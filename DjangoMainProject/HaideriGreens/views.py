from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages

# Super user details:
# Name: IdrisAdmin
# Password: Vohra987

globContext= {
    "Email": "",
    "FirstName": "",
    "LastName": "",
    "Password": ""
}
# Create your views here.
def index(request):
    # If the user credentials does not exist it should open the Invalid modal
    if request.method == 'POST':
        if request.user.is_anonymous:
            messages.warning(request,"Invalid details!","Consider signing-up")
        else:
            messages.success(request,"Successfully logged in!")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        uname = request.POST.get('username')

def about(request):
    return render(request, 'about.html')

def visit(request):
    return render(request, 'visit.html')

def signup(request):
    
    return render(request, 'signup.html')

def products(request):
    return render(request, 'products.html')

def basket(request):
    return render(request, 'basket.html')

def donate(request):
    return render(request, 'donate.html')
