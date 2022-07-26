

from django.shortcuts import redirect, render
from .forms import FormCliente, FormFornecedor, FormTpPessoa, FormUsuario
from .models import Cliente, Fornecedor, TpPessoa, Usuario

# Create your views here.
def lista_tp_pessoas(request):
    tipoPessoa = TpPessoa.objects.all()
    total = tipoPessoa.count
    return render(request,'lista_tp_pessoa.html',{ 'tipos' : tipoPessoa, 'total' : total })

def cadastra_tp_pessoa(request):
    if request.method == 'POST':
        form = FormTpPessoa(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoas)
    return render(request,'cadastra_tp_pessoa.html')

def altera_tp_pessoa(request):
    return render(request,'altera_tp_pessoa.html')

def exclui_tp_pessoa(request):
    return render(request,'exclui_tp_pessoa.html')            

def lista_clientes(request):
    cliente = Cliente.objects.all()
    total = cliente.count
    return render(request,'lista_clientes.html',{'cliente' : cliente, ' total ' : total })

def cadastra_cliente(request):
    tp_pessoa = TpPessoa.objects.all()
    if request.method == 'POST':
        form = FormCliente(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request,'cadastra_cliente.html',{'tipo' : tp_pessoa})

def altera_cliente(request):
    return render(request,'altera_cliente.html')

def exclui_cliente(request):
    return render(request,'exclui_cliente.html')            

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    total = fornecedores.count
    return render(request,'lista_fornecedores.html', { 'fornecedores' : fornecedores, 'total' : total })

def cadastra_fornecedor(request):
    tipo = TpPessoa.objects.all()
    if request.method == 'POST':
        form = FormFornecedor(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)
    return render(request,'cadastra_fornecedor.html',{'tipos' : tipo})

def altera_fornecedor(request):
    return render(request,'altera_fornecedor.html')

def exclui_fornecedor(request):
    return render(request,'exclui_fornecedor.html')            

def lista_usuarios(request):
    usuario = Usuario.objects.all()
    total = usuario.count
    return render(request,'lista_usuarios.html',{ 'usuario' : usuario, 'total' : total })

def cadastra_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(lista_usuarios)
    return render(request,'cadastra_usuario.html')

def altera_usuario(request):
    return render(request,'altera_usuario.html')

def exclui_usuario(request):
    return render(request,'exclui_usuario.html')                
