from pyexpat import model
from django.db import models

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)
    
    def __str__(self):
        return self.num_doc
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    #relação de um para um quando cada um objeto é ligado ao outro e não poderá ser ligado para outro.    
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)       

#o que vai retornar
    def __str__(self):
        return self.first_name+' '+self.last_name
    
class Produto(models.Model):    
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao

# FIXME: teste

class Venda(models.Model):
    numero = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    impostos = models.DecimalField(max_digits=8, decimal_places=2)
    desconto = models.DecimalField(max_digits=8, decimal_places=2)
    #Aqui não vai poder deletar a pessoa sem deletar antes as vendas, está protegido.
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)
    
    #TODO: refatorar para usar thredes
    def __str__(self):
        return self.numeropy