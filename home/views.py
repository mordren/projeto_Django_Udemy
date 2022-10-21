from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='../../login/')
def home(request):          
    return render(request, 'home/home.html')
    

def my_logout(request):
    logout(request)
    return redirect('home')