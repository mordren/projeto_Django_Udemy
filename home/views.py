from cgi import test
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    #necessário trocar o template_name para funcionar
    template_name = "home/home3.html"
    def get_context_data(self, **kwargs):
        #recebe o context de herança da classe pai
        context = super().get_context_data(**kwargs)
        
        #envio ao template através do context alguma informação.        
        context['test'] = 'asdrubal'
        return context

# Create your views here.
@login_required(login_url='../../login/')
def home(request):         
    #import pdb; pdb.set_trace()
    return render(request, 'home/home.html')

def my_logout(request):
    logout(request)
    return redirect('home')