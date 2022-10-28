from msilib.schema import ListView
from time import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Person
from .forms import PersonForm
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def hello(request):
    return render(request, 'clientes/index.html')

def fname2(request, nome):
    data = {}
    id = Person.objects.get(first_name=nome).pk
    pessoa = Person.objects.get(pk=id)
    data['pessoa'] = pessoa
    return render(request, 'clientes/pessoa.html', data)

@login_required(login_url='../../login/')
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'clientes/person.html', {'persons':persons})

@login_required(login_url='../../login/')
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'clientes/person_form.html', {'form':form})

@login_required(login_url='../../login/')
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    #envia o form com todos os dados
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    #se o form é valido, ou seja, não está vazio ele salvar
    if form.is_valid():
        form.save()
        return redirect('person_list')
    #se não ele cria o formulário para ser populado.    
    return render(request, 'clientes/person_form2.html', {'form': form})

@login_required(login_url='../../login/')
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    #nesse eu envio uma pessoa para criar uma instância lá no template, para decidir se vou deletar.        
    person.delete()
    return redirect('person_list')

class ModelListView(ListView):
    model = Person
    
class PersonDetail(DetailView):    
    model = Person        
    
class PersonCreate(CreateView):
    model = Person
    # aqui são listados os campos que eu quero criar o model
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list2')
    
class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list2')
    
class PersonDelete(DeleteView):
    #apenas colocar o delete    
    model = Person    
    success_url = reverse_lazy('person_list2')
    
    def get_success_url(self):
        #aqui podemos fazer o que quiser com o usuário;
        #podemos fazer alguma verificação à mais;        
        success_url = reverse_lazy('person_list2')