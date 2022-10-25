from telnetlib import DO
from django.contrib import admin
from .models import Person, Documento, Venda
# Register your models here.

admin.site.register(Person)
admin.site.register(Documento)
admin.site.register(Venda)