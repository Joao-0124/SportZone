from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Produto

def index(request):
    produtos = Produto.objects.order_by('nome')
    context = {'produtos': produtos}
    return render(request, 'index.html', context)

