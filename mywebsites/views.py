from django.shortcuts import render
from .models import Mywebsites

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def contact(request):
    return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def service(request):
    return render(request,'service.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def registration(request):
    return render(request,'registration.html',{})

def submit_form_method(request):
    print('Submit method is called')
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    birthday = request.POST["birthday"]
    gender = request.POST["gender"]
    email = request.POST["email"]
    phone = request.POST["phone"] 
    address_local = request.POST["address_local"]
    address_permanent = request.POST["address_permanent"]
    subject = request.POST["subject"]

    my_registration = Mywebsites(first_name=first_name,last_name=last_name, birthday=birthday, gender=gender, email=email, phone=phone,address_local=address_local, address_permanent=address_permanent)
    my_registration.save()
    print('Bhanu Values : '+first_name+'  '+last_name+' '+birthday+' '+gender+' '+email+' '+phone+' '+address_local+' '+address_permanent+' '+subject)
    return render(request,'registration.html',{})
