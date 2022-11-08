from telnetlib import DO
from django.contrib import admin
from .models import Person, Documento, Venda, Produto
from .actions import nfe_emitida
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    #fields = ['doc','first_name', 'last_name', 'salary', 'photo']    
    #fields = ['doc',('first_name', 'last_name'), ('salary', 'photo')]    
    
    #Cria-se faixas dentro do cadastro, criando-assim blocos.
    fieldsets = (
        ('Dados Principais', {
            'fields': ('first_name','last_name','age')
        }),
        ('Dados Avançados', {
            'fields':('salary','photo','doc'),
        }))
    list_display = ('first_name', 'last_name', 'salary', 'tem_foto','doc')
    #mostra um filtro ao lado do admin:
    list_filter = ('age','salary')
    search_fields = ('id','first_name')
    

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
        
    tem_foto.short_description = 'Possui Foto'
    
class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    list_display = ('numero','pessoa', 'total', 'nfe_emitida')
    search_fields = ('id', 'numero', 'pessoa__first_name', 'pessoa__doc__num_doc',)
    autocomplete_fields = ('pessoa','produtos',)
    actions = [nfe_emitida]
    #filter_vertical = ['produtos']
    
    def total(self, obj):
        return obj.get_total()
    
    total.short_description = 'Total'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor')
    search_fields = ('id','descricao')
    
#altera o texto do django admin
admin.site.site_header = 'Gestão de clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Seja bem vindo ao administrador'
    
admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)