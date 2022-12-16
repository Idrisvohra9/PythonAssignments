from django.shortcuts import render
from django.http import HttpResponse
from .models import FormModel
# Create your views here.
def index(request):
    # params = {"Name": request.GET.get('name')}
    # print(request.GET.get('name'))
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["e"]
        password = request.POST["p"]

        obj = FormModel()
        obj.fname = fname
        obj.lname = lname
        obj.email = email
        obj.password = password
        obj.save()
        data = FormModel.objects.all()
        
        context = {
            "fname": fname,
            "lname": lname,
            "email": email,
            "password": password,
            "data": data
        }
        print(context)
    return render(request, "index.html")
    # This statement below sends a response message to the website
    # return HttpResponse("This is Home page.")

# Similarly renders about page
def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')
