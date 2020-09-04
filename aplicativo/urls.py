from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('interno/', views.interno, name='interno'),
    path('externo/', views.externo, name='externo'),
    path('', views.login, name='login_index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('ver_relatorio/<int:relatorio_id>', views.ver_relatorio, name='ver_relatorio'),
    path('update/<int:relatorio_id>', views.update),
    path('busca/', views.busca, name='busca'),
    path('saida/<int:relatorio_id>', views.saida, name='saida'),
    path('saida_doc/<int:relatorio_id>', views.saida_doc, name='saida_doc'),
]