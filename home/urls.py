from django.urls import path
from django.views import View
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.my_logout, name='logout'),
    path('home2', TemplateView.as_view(template_name='home/home2.html'), name='home3'),
    path('home3', views.HomePageView.as_view(), name='home3'),
    path('view', views.MyView.as_view(), name='view')    
]