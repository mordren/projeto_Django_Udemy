from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('', persons_list, name='person_list'), 
   path('new/', persons_new, name='persons_new'),
   path('update/<int:id>/', persons_update, name='persons_update'),
   path('delete/<int:id>/', persons_delete, name='persons_delete'),
   path('person_list', ModelListView.as_view(), name='person_list2'),
   path('person_detail/<int:pk>/', PersonDetail.as_view(), name='person_detail'),
   path('person_create', PersonCreate.as_view(), name='person_create'),   
   path('person_update/<int:pk>/', PersonUpdate.as_view(), name='person_update'),   
   path('person_delete/<int:pk>/', PersonDelete.as_view(), name='person_delete'),   
]

