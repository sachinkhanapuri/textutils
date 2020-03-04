from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import customer
from django.http import Http404


# Create your views here.
def homepage(request):
    return render(request,'home.html')

# instering data into database from front-end with help of form method
def add_data(request):
    if request.method=="POST":
        name1=request.POST["name"]
        emailid1=request.POST["emailid"]
        contact1=request.POST["contact"]
        gender1=request.POST["gender"]
        data=customer(name=name1,emailid=emailid1,contactno=contact1,gender=gender1)
        data.save()
        return render(request,'home.html')

# fetching details from database and display on HTML page
def display(request):
    obj=customer.objects.all()
    context={
           'object':obj
          }
    return render(request,'display.html',context)

# fetching a particular details from database with customer id
def display_item(request,id):
    try:
        obj=customer.objects.get(id=id)
    except customer.DoesNotExist:
        raise Http404 
    context={
            'object':obj
        }
    return render(request,'create.html',context)


