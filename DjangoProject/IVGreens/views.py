from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def visit(request):
    return render(request, 'visit.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def products(request):
    return render(request, 'products.html')
