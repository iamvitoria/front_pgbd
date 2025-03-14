# agendamento/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from agendamento.models import Agendamento
from restaurante.models import CardapioRestaurante, Restaurante
from agendamento.forms import AgendamentoForm, RestauranteSelectForm
from django.contrib.auth.decorators import login_required
from financeiro.models import Transacao, Carteira
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
def selecionar_restaurante(request):
    if request.method == "POST":
        form = RestauranteSelectForm(request.POST)
        if form.is_valid():
            restaurante_id = form.cleaned_data['restaurante'].id
            return redirect('agendar', restaurante_id=restaurante_id)
    else:
        form = RestauranteSelectForm()

    return render(request, 'agendamento/selecionar_restaurante.html', {'form': form})

@login_required
def agendar(request, restaurante_id):
    if request.method == "POST":
        form = AgendamentoForm(restaurante_id=restaurante_id, data=request.POST)
        if form.is_valid():

            carteira = Carteira.objects.get(usuario=request.user)

            print("Saldo carteira: ", carteira.saldo)
            print("Valor refeicao: ", form.cleaned_data['cardapio_agendado'].cardapio.refeicao.valor)

            if carteira.saldo < form.cleaned_data['cardapio_agendado'].cardapio.refeicao.valor:
                messages.error(request, 'Saldo insuficiente para realizar o agendamento.')
                return redirect('agendar', restaurante_id=restaurante_id)

            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.save()


            Transacao.objects.create(
                carteira=carteira,
                valor=agendamento.cardapio_agendado.cardapio.refeicao.valor,
                is_entrada=False
            )
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('ver_agendamentos')
    else:
        form = AgendamentoForm(restaurante_id=restaurante_id)

    cardapios = CardapioRestaurante.objects.filter(restaurante_id=restaurante_id)

    restaurante = Restaurante.objects.get(id=restaurante_id)

    return render(request, 'agendamento/agendar.html', {'form': form, 'cardapios': cardapios, 'restaurante': restaurante})

@login_required
def ver_agendamentos(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    return render(request, 'agendamento/ver_agendamentos.html', {'agendamentos': agendamentos})


@csrf_exempt
def cancelar_agendamento(request, agendamento_id):
    if request.method == "POST":
        try:
            agendamento = get_object_or_404(Agendamento, id=agendamento_id)
            agendamento.delete()
            return JsonResponse(
                {"status": "success", "message": "Agendamento cancelado com sucesso."}
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": f"Erro ao cancelar: {str(e)}"},
                status=500,
            )
    return JsonResponse(
        {"status": "error", "message": "Método não permitido."}, status=405
    )
