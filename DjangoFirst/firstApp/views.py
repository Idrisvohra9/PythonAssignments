from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    params = {"Name": request.GET.get('name')}
    print(request.GET.get('name'))
    # Get template:
    # template = loader.get_template('index.html')
    # Render the index.html file here:
    return render(request, "index.html", params)
    # This statement below sends a response message to the website
    # return HttpResponse("This is Home page.")

# Similarly renders about page
def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')

