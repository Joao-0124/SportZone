from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Produto, Categoria, Compra, CompraProdutoItem, Cliente

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

def registro_cliente(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            endereco_residencial = f"{request.POST['rua']}, {request.POST['numero']}, {request.POST['complemento']}, {request.POST['bairro']}, {request.POST['cep']}, {request.POST['cidade']}, {request.POST['estado']}, {request.POST['pais']}"
            cliente = Cliente(
                nome=request.POST['nome'],
                email=request.POST['email'],
                telefone=request.POST['telefone'],
                cpf=request.POST['cpf'],
                endereco_residencial=endereco_residencial
            )
            cliente.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()
    
    return render(request, 'registro_cliente.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirecionar para a página inicial após o login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
