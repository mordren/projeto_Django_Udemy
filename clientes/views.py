from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm

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
    return render(request, 'clientes/person_form.html', {'form': form})

@login_required(login_url='../../login/')
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    #nesse eu envio uma pessoa para criar uma instância lá no template, para decidir se vou deletar.        
    person.delete()            
    return redirect('person_list')    