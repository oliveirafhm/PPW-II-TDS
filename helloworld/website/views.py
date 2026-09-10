from django.shortcuts import render
from helloworld.models import Funcionario

from django.views.generic import ListView

# Apenas para teste neste momento
def index(request):
    return lista_funcionarios(request)

def cria_funcionario(request):
    # Verificamos se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_funcionarios'))

    # Qualquer outro método: GET, OPTION, DELETE etc...
    else:
        return render(request, "website/form.html", {'form':form})

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()

    #Incluímos no contexto
    contexto = {'funcionarios': funcionarios}

    # Retornamos o template para listar os funcionários
    return render(request, "website/funcionarios.html", contexto)

class ListaFuncionarios(ListView):
    template_name = "website/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"