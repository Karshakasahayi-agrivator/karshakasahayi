from django.shortcuts import render
from .forms import orderform
from .models import Order

def index(request):
    if request.method=='POST':
        form=orderform(request.POST)
        if form.is_valid():
            obj=Order()
            obj.name=form.cleaned_data['name']
            obj.phone=form.cleaned_data['phone']
            obj.email=form.cleaned_data['email']
            obj.address=form.cleaned_data['address']
            obj.date_required=form.cleaned_data['date_required']
            obj.save()
            return render(request,'submit.html')
        else:
            form=orderform()
    else:
        return render(request,'index.html')
        
