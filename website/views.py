from django.shortcuts import render


def index(request):
    if request.method=='POST':
        return render(request,'submit.html')
    else:
        return render(request,'index.html')
        
