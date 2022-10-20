from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.
def home(request):       
    return render(request, 'home/home.html')

def my_logout(request):
    logout(request)
    return redirect('home')