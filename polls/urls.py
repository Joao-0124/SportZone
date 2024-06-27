from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:produto_id>/', views.produto_detail, name='produto_detail'),
    path('carrinho_compra/', views.carrinho_compra, name='carrinho_compra'),  # Defina a URL para carrinho_compra
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_cliente, name='registro_cliente'),

    # Outras URLs do seu aplicativo
]
