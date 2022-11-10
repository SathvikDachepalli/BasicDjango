import datetime
from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from datetime import date
def index(request):

    messages.success(request,"Welcome to my website")
    return render(request,template_name="jumbo.html")
def about(request):
    return HttpResponse("This is about ")
def Services(request):
    return HttpResponse("This is services")
def jumbo(request):
    return render(request,template_name="jumbo.html")
def base(request):
    return render(request,template_name="base.html")
def test(request):
    content={
        'variable':"Test",
        'name':"Sathvik",
    }
    return render(request,template_name='test.html',context=content)
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc =request.POST.get('Review')
        date =datetime.datetime.today()

        if name=="" or email=="" or phone=="" or desc=="":
            messages.error(request,"It is not delivered")
        else:
            contact=Contact(name=name,email=email,phone=phone,desc=desc,date=date)
            contact.save()
            messages.success(request,'Your message has been sent')
            return HttpResponseRedirect(request.path)
            
    return render(request,template_name='contact.html')