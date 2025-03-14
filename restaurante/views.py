from .models import Restaurante, Refeicao
from agendamento.models import Agendamento
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DefinirLimiteAgendamentosForm, AssociarCardapioForm, GerarRelatorioForm
from django.contrib.auth.decorators import login_required

@login_required
def verificar_agendamentos_semana(request, restaurante_id):
    agendamentos_semana = Agendamento.objects.filter(
        data_agendamento__week=timezone.now().isocalendar()[1],
        cardapio_agendado__restaurante=Restaurante.objects.get(pk=restaurante_id),
    )
    quantia_agendamentos_semana = agendamentos_semana.count()

    comidas_mais_agendadas = {}
    for agendamento in agendamentos_semana:
        if agendamento.cardapio_agendado not in comidas_mais_agendadas:
            comidas_mais_agendadas[agendamento.cardapio_agendado] = 1
        else:
            comidas_mais_agendadas[agendamento.cardapio_agendado] += 1

    quantia_uso_dias = {}
    # montar

    if agendamentos_semana.exists():
        return render(request, "restaurante/ver_agendamentos_semana.html", {"agendamentos_semana": agendamentos_semana})

    return render(request, "restaurante/sem_agendamentos.html")

@login_required
def definir_limite_agendamentos(request, refeicao_id):
    refeicao = get_object_or_404(Refeicao, id=refeicao_id)

    if request.method == "POST":
        form = DefinirLimiteAgendamentosForm(request.POST, instance=refeicao)
        if form.is_valid():
            form.save()
            return redirect("ver_refeicoes")
    else:
        form = DefinirLimiteAgendamentosForm(instance=refeicao)

    return render(
        request,
        "restaurante/definir_limite_agendamentos.html",
        {"form": form, "refeicao": refeicao},
    )

@login_required
def associar_cardapio_ao_restaurante(request):
    if request.method == "POST":
        form = AssociarCardapioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "ver_agendamentos"
            ) 
    else:
        form = AssociarCardapioForm()

    return render(request, "restaurante/associar_cardapio.html", {"form": form})

def gerar_relatorios(request):
    agendamentos_feitos = porcentagem_uso = refeicao_mais_agendada = None

    if request.method == "POST":
        form = GerarRelatorioForm(request.POST)
        if form.is_valid():
            agendamentos_feitos, porcentagem_uso, refeicao_mais_agendada = form.save()
    else:
        form = GerarRelatorioForm()

    context = {
        "form": form,
        "agendamentos_feitos": agendamentos_feitos,
        "porcentagem_uso": porcentagem_uso,
        "refeicao_mais_agendada": refeicao_mais_agendada,
    }

    return render(request, "restaurante/gerar_relatorios.html", context)

def ver_refeicoes(request):
    refeicoes = Refeicao.objects.all()
    return render(request, 'restaurante/ver_refeicoes.html', {'refeicoes': refeicoes})
