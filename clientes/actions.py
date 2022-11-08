
#muda as actions dentro do nossa lista de vendas.
def nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)
    
nfe_emitida.short_description = "NF-e emitida"