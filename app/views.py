from django.shortcuts import render

# Create your views here.


def usd(request):
    d={'data':'hai harshad hoe are you'}
    return render(request,'usd.html',d)