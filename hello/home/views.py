from home.models import Contact
from django.shortcuts import render,HttpResponse
from datetime import datetime
from django.contrib import messages
 
# Create your views here.
def index(request):
    context = {
    'variable':"ALLAH is great"
    }
    messages.success(request, 'OFFER OFFER OFFER')
    return render(request,'index.html',context)
    

    #return HttpResponse("This is Home page  Nice")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
def icecream(request):
    return render(request,'services/Ice-Cream.html')
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        date=request.POST.get('date')
        contact=Contact(name=name,phone=phone,email=email,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Detail has been Stored!')

    return render(request,'contact.html')