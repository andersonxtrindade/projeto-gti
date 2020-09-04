from .models import Relatorio, FormRelatorio
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404

def login(request):
    if request.method != 'POST':
        return render(request, 'aplicativo/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        return render(request, 'aplicativo/login.html')

    else:
        auth.login(request, user)
        return redirect('index')


@login_required(redirect_field_name='login')
def index(request):
    return render(request, 'aplicativo/index.html')


def lista(request):
    relatorios = Relatorio.objects.order_by('-id')
    paginator = Paginator(relatorios, 15)

    page = request.GET.get('p')
    relatorios = paginator.get_page(page)
    return render(request, 'aplicativo/listaRelatorios.html',{
        'relatorios': relatorios
    })


@login_required(redirect_field_name='login')
def interno(request):
    if request.method != 'POST':
        form = FormRelatorio()
        return render(request, 'aplicativo/interno.html', {'form': form})

    form = FormRelatorio(request.POST, request.FILES)

    if not form.is_valid():
        form = FormRelatorio(request.POST)
        return render(request, 'aplicativo/interno.html', {'form': form})

    form.save()
    return redirect('lista')


@login_required(redirect_field_name='login')
def externo(request):
    return render(request, 'aplicativo/externo.html')

@login_required(redirect_field_name='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(redirect_field_name='login')
def ver_relatorio(request, relatorio_id):
    relatorio =Relatorio.objects.get(id=relatorio_id)
    return render(request, 'aplicativo/ver_relatorio.html', {
        'relatorio': relatorio
    })

@login_required(redirect_field_name='login')
def update(request, relatorio_id):
    relatorio = Relatorio.objects.get(id=relatorio_id)
    form = FormRelatorio(data=request.POST, instance=relatorio)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect("/lista")
    return render(request, 'aplicativo/ver_relatorio.html', {
            'relatorio': relatorio
        })

@login_required(redirect_field_name='login')
def busca(request):
    termo = request.GET.get('termo')
    relatorios = Relatorio.objects.order_by('-id').filter(
        Q(sessp__icontains=termo) | Q(patrimonio__icontains=termo) | Q(serie__icontains=termo) | Q(num_chamado__icontains=termo)
    )
    paginator = Paginator(relatorios, 15)

    page = request.GET.get('p')
    relatorios = paginator.get_page(page)
    return render(request, 'aplicativo/listaRelatorios.html', {
        'relatorios': relatorios
    })

def saida(request, relatorio_id):
    relatorio = Relatorio.objects.get(id=relatorio_id)
    return render(request, 'aplicativo/saida.html', {
        'relatorio': relatorio
    })

def saida_doc(request, relatorio_id):
    relatorio = Relatorio.objects.get(id=relatorio_id)
    return render(request, 'aplicativo/saida_doc.html', {
        'relatorio': relatorio
    })

