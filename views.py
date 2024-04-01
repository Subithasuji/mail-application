from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def mail(request):
    subject='Django-Greetings'
    msg='Welcome Shalini, congrats for your successfull mail setup'
    to='shalinistellus@gmail.com'
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if(res==1):
        msg='mail send successfully'
    else:
        msg='mail not send successfully'
    return HttpResponse(msg)

# Create your views here.
