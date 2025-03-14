from django.shortcuts import render
from django.utils import timezone
from restaurante.models import CardapioRestaurante
from cardapio.models import Cardapio
from datetime import timedelta
from agendamento.forms import RestauranteSelectForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def selecionar_restaurante(request):
    if request.method == "POST":
        form = RestauranteSelectForm(request.POST)
        if form.is_valid():
            restaurante_id = form.cleaned_data["restaurante"].id
            return redirect("ver_cardapio_semana", restaurante_id=restaurante_id)
    else:
        form = RestauranteSelectForm()

    return render(request, "agendamento/selecionar_restaurante.html", {"form": form})

@login_required
def ver_cardapio(request, restaurante_id):
    cardapio_rest = CardapioRestaurante.objects.get(id=restaurante_id).cardapio
    return render(request, 'cardapio/ver_cardapio.html', {"cardapio": cardapio_rest, "restaurante_id": restaurante_id})

@login_required
def ver_cardapio_semana(request, restaurante_id):
    data_atual = timezone.now().date()
    dia_da_semana = data_atual.weekday()

    dias_ate_sexta = 4 - dia_da_semana if dia_da_semana <= 4 else 0
    proxima_sexta = data_atual + timedelta(days=dias_ate_sexta)

    cardapios_semana = CardapioRestaurante.objects.filter(
        restaurante_id=restaurante_id,
        data_oferecida__range=[data_atual, proxima_sexta]
    ).order_by('data_oferecida', 'cardapio__refeicao__horario_abertura')

    cardapios_por_dia = {}
    for cardapio_restaurante in cardapios_semana:
        dia = cardapio_restaurante.data_oferecida
        if dia not in cardapios_por_dia:
            cardapios_por_dia[dia] = []
        cardapios_por_dia[dia].append(cardapio_restaurante)

    return render(request, 'cardapio/ver_cardapio_semana.html', {"cardapios_por_dia": cardapios_por_dia, "restaurante_id": restaurante_id, "restaurante_nome": CardapioRestaurante.objects.get(id=restaurante_id)})
