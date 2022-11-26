"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import inicio, home, form, create, view, edit, update, delete, homeCliente, formCliente, createCliente, viewCliente, editCliente, updateCliente, deleteCliente, lista_produto, lista_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('home/', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    # path('pdf/', pdf, name='pdf'),
    path('lista_produto/', lista_produto, name='lista_produto'),
    
    #cadastro cliente
    
    path('homeCliente/', homeCliente, name='homeCliente'),
    path('formCliente/', formCliente, name='formCliente'),
    path('createCliente/', createCliente, name='createCliente'),
    path('viewCliente/<int:pk>/', viewCliente, name='viewCliente'),
    path('editCliente/<int:pk>/', editCliente, name='editCliente'),
    path('updateCliente/<int:pk>/', updateCliente, name='updateCliente'),
    path('deleteCliente/<int:pk>/', deleteCliente, name='deleteCliente'),
    path('lista_cliente/', lista_cliente, name='lista_cliente'),
    
    
 
    
]
