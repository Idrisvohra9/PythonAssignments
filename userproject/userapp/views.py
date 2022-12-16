from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages

# usrname : Aryan
# Password : Ar@03052003

# Create your views here.

def index(request):
    context = {
        "var" : []
    }
    for i in range(0,10):
        context["var"].append(i+1);
    # When user 
    if request.user.is_anonymous:
        messages.warning(request,"Invalid details!","Consider signing-up")
    return render(request, 'index.html',context)
    
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html') 
    return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect("/login")
