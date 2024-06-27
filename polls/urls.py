from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:produto_id>/', views.produto_detail, name='produto_detail'),
    path('carrinho_compra/', views.carrinho_compra, name='carrinho_compra'),  # Defina a URL para carrinho_compra

    # Outras URLs do seu aplicativo
]
