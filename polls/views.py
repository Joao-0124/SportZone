from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produto, Categoria, Compra, CompraProdutoItem

def index(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'index.html', context)

def produto_detail(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    context = {
        'produto': produto,
    }
    return render(request, 'produto_detail.html', context)

def carrinho_compra(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, pk=produto_id)
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'carrinho_compra.html')

def adicionar_ao_carrinho(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = int(request.POST.get('quantidade', 1)) 
        produto = get_object_or_404(Produto, pk=produto_id)
        compra, _ = Compra.objects.get_or_create(cliente=request.user, status='em andamento')
      
        item_existente = compra.compraprodutoitem_set.filter(produto=produto).first()
        if item_existente:
            item_existente.quantidade += quantidade
            item_existente.save()
        else:
            novo_item = CompraProdutoItem(compra=compra, produto=produto, quantidade=quantidade, valor=produto.preco_venda)
            novo_item.save()
        
        return redirect('produto_detail', produto_id=produto_id)
    return redirect('pagina_principal')  

