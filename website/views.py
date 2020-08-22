from django.shortcuts import render
from .forms import orderform
from .models import Order
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method=='POST':
        form=orderform(request.POST)
        if form.is_valid():
            obj=Order()
            obj.name=form.cleaned_data['name']
            obj.phone=form.cleaned_data['phone']
            obj.email=form.cleaned_data['email']
            obj.address=form.cleaned_data['address']
            obj.workers=form.cleaned_data['workers']
            obj.date_required=form.cleaned_data['date_required']
            obj.save()
            #send mail
            email_from=settings.EMAIL_HOST_USER
            email_to=[obj.email,]
            content='Hi '+ obj.name + ',\nYour application is recorded and the workers will be alloted as per reqirement and availability.\nRegards,\nKarshakasahayi Agrivator'
            send_mail(
                'Karshakasahayi',
                 content,
                 email_from,
                 email_to)
            
            return render(request,'submit.html')
        else:
            form=orderform()
    else:
        return render(request,'index.html')
        
