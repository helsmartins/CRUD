from django.shortcuts import render, redirect
from app.forms import OculosForm, ClienteForm
from app.models import Oculos, Clientes
import io 
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.
def lista_produto(request):
    template_name = 'cadastro_produto/index.html'
    object = Oculos.objects.all()
    search = request.Get.get('search')
    if  search:
        objects = objects.filter(marca_icontains=search)
        context = {'': objects}
    return render(request, template_name, object, context)

def lista_cliente(request):
    template_name = 'cadastro_cliente/index.html'
    object = Clientes.objects.all()
    search = request.Get.get('search')
    if  search:
        objects = objects.filter(nome_icontains=search)
        context = {'': objects}
    return render(request, template_name, object, context)

# def pdf(request):
#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer)
#     p.drawString(100, 800, '{}.pdf')
#     p.showPage()
#     p.save()
#     buffer.seek(0)
#     return FileResponse(request, buffer, as_attachment=True,  filename='relatório.pdf')
      
         
# Cadastro Produto

def inicio(request):
    return render(request, 'main.html')

def home(request):
    data = {}
    data['db'] = Oculos.objects.all()
    return render(request, 'cadastro_produto/index.html', data)

def form(request):
    data = {}
    data['form'] = OculosForm()
    return render(request, 'cadastro_produto/form.html', data)

def create(request):
    form = OculosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Oculos.objects.get(pk=pk)
    return render(request, 'cadastro_produto/view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Oculos.objects.get(pk=pk)
    data['form'] = OculosForm(instance=data['db'])
    return render(request, 'cadastro_produto/form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Oculos.objects.get(pk=pk)
    form = OculosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Oculos.objects.get(pk=pk)
    db.delete()
    return redirect( 'home')

# Cadastro Cliente

def homeCliente(request):
    data = {}
    data['db'] = Clientes.objects.all()
    return render(request, 'cadastro_cliente/index.html', data)


def formCliente(request):
    data = {}
    data['formCliente'] = ClienteForm()
    return render(request, 'cadastro_cliente/form.html', data)

def createCliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('homeCliente')
    
def viewCliente(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    return render(request, 'cadastro_cliente/view.html', data)

def editCliente(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    data['formCliente'] = ClienteForm(instance=data['db'])
    return render(request, 'cadastro_cliente/form.html', data)

def updateCliente(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('homeCliente')
    
def deleteCliente(request, pk):
    db = Clientes.objects.get(pk=pk)
    db.delete()
    return redirect('homeCliente')