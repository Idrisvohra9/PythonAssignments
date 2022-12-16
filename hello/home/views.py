from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Product
from django.urls import reverse
# Create your views here.
def index(request):

    context={
        "variable": "my name is sujal"
    }
    # template=loader.get_template('index.html')
    # return HttpResponse(template.render(),context)
    data=Product.objects.all()
    return render(request, 'index.html',{"data":data})
    # to print the text directly on the page
    # return HttpResponse("this is index page")

# def about(request):
    # return render(request,'about.html')
    # return HttpResponse("this is about page")
# def login(request):
    # return render(request,'login.html')
    # return HttpResponse("this is login page")
# def contact(request):
    # return render(request,'contact.html')
    # return HttpResponse("this is contact page")
# def services(request):
    # return render(request,'services.html')
    # return HttpResponse("this is services page")
def test(request):
    if request.method=='POST':
        name=request.POST['name']
        type =request.POST['type']
        description=request.POST['description']
        obj=Product()
        obj.name=name
        obj.type=type
        obj.description=description
        obj.save()
    data=Product.objects.all()
    if request.method=='POST':
        # return render(request, ':index.html',{"data":data})
        print("if")
        return HttpResponseRedirect('/login')
    else:
        print("else")
        return render(request, 'index.html',{"data":data})
    


# delete    
def delete(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/login')


# update
def update(request,id):
    data=Product.objects.get(id=id)
    temp=loader.get_template('update.html')
    context={
        'data':data
    }
    return HttpResponse(temp.render(context,request))

# update record
def updaterecord(request,id):
    name=request.POST['name']
    type =request.POST['type']
    data=Product.objects.get(id=id)
    data.name=name
    data.type=type
    data.save()
    return HttpResponseRedirect(reverse('index'))
    # if request.method=='POST':
    #     # Product=Product.object.filter(id=id)
    #     # Product.name=name
    #     # Product.type=type
    #     name= request.POST['name']
    #     type= request.POST['type']
    #     # print(name)
    #     # print(type)
    #     # print(name)
    #     obj=Product()
    #     obj.name=name
    #     obj.type=type
    #     obj.save()
    
    # return render(request,"index.html",{"data":data})
    # return HttpResponseRedirect('/index')


    #  to add two number
# def add(request):
#     a=int(request.POST['num1'])
#     b=int(request.POST['num2'])
#     c=a+b
#     return render(request,'result.html',{"result":c})