from django.contrib import admin
from django.urls import path
from clientes.views import hello, fname2
from .views import persons_list, persons_new, persons_update, persons_delete

urlpatterns = [
   path('', persons_list, name='person_list'), 
   path('new/', persons_new, name='persons_new'),
   path('update/<int:id>/', persons_update, name='persons_update'),
   path('delete/<int:id>/', persons_delete, name='persons_delete'),
]

