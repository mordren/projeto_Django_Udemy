from django.contrib import admin
from django.urls import path
from clientes.views import hello, fname2
from .views import *

urlpatterns = [
   path('', persons_list, name='person_list'), 
   path('new/', persons_new, name='persons_new'),
   path('update/<int:id>/', persons_update, name='persons_update'),
   path('delete/<int:id>/', persons_delete, name='persons_delete'),
   path('person_list', ModelListView.as_view(), name='person_list2'),
   path('person_detail/<int:pk>/', PersonDetail.as_view(), name='person_detail'),
]

