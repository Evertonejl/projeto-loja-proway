from django.shortcuts import redirect, render
from .forms import FormCategoria, FormItem
from .models import Categoria, Item

# Create your views here.
def lista_categorias(request):
    categorias = Categoria.objects.all()
    total = categorias.count
    return render(request,'lista_categorias.html', { 'categorias': categorias, 'total' : total })

def cadastra_categoria(request):
    form = FormCategoria(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_categorias)
    return render(request,'cadastra_categoria.html')

def altera_categoria(request):
    return render(request,'altera_categoria.html')

def exclui_categoria(request):
    return render(request,'exclui_categoria.html')    

def lista_itens(request):
    return render(request,'lista_intens.html')

def cadastra_item(request):
    return render(request,'cadastra_item.html')

def altera_item(request):
    return render(request,'altera_item.html')

def exclui_item(request):
    return render(request,'exclui_item.html')               

