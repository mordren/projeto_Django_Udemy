from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver 

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)
    
    def __str__(self):
        return self.num_doc
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    bio = models.TextField(null=True, blank=True)
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
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    impostos = models.DecimalField(max_digits=8, decimal_places=2)
    desconto = models.DecimalField(max_digits=8, decimal_places=2)
    #Aqui não vai poder deletar a pessoa sem deletar antes as vendas, está protegido.
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)
    nfe_emitida = models.BooleanField(default=False)
    
    def get_total(self):
        tot = 0
        for produto in self.produtos.all():
            tot += produto.valor
        
        return (tot - self.desconto)-self.impostos
    #TODO: refatorar para usar thredes    
    def __str__(self):
        return self.numero

#isso aqui não funcionou muito bem, esse tipo de coisa 
#tem que pesquisar melhor na internet como colocar campos depois do registro
@receiver(m2m_changed, sender=Venda.produtos.through)
def update_vendas_total(sender, instance, **kwargs):
    instance.valor = instance.get_total()
    instance.save()