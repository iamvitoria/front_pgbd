from django import forms
from .models import CardapioRestaurante, Refeicao
from cardapio.models import Cardapio
from restaurante.models import Restaurante
from agendamento.models import Agendamento

class DefinirLimiteAgendamentosForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = ["nome", "limite_agendamentos"]
        labels = {
            "nome": "Nome refeição",
            "limite_agendamentos": "limite de agendamentos",
        }
        widgets = {
            "nome": forms.Select(attrs={"class": "form-control"}),
            "limite_agendamentos": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "placeholder": "bote o limite de agendamentos",
                }
            ),
        }

    def clean_limite_agendamentos(self):
        limite = self.cleaned_data["limite_agendamentos"]
        if limite <= 0:
            raise forms.ValidationError("The limit must be greater than 0.")
        return limite

class AssociarCardapioForm(forms.ModelForm):
    class Meta:
        model = CardapioRestaurante
        fields = ["data_oferecida", "cardapio", "restaurante"]
        labels = {
            "data_oferecida": "data oferecida",
            "cardapio": "cardapio",
            "restaurante": "Restaurante",
        }
        widgets = {
            "data_oferecida": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "cardapio": forms.Select(attrs={"class": "form-control"}),
            "restaurante": forms.Select(attrs={"class": "form-control"}),
        }

class GerarRelatorioForm(forms.Form):
    restaurante = forms.ChoiceField(choices=Restaurante.objects.values_list('id', 'nome'))
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tipo_refeicao = forms.ChoiceField(choices=Refeicao.objects.values_list('nome', 'nome'))
    data_fim = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        fields = ['restaurante', 'data_inicio', 'tipo_refeicao', 'data_fim']

    def save(self):
        restaurante = self.cleaned_data["restaurante"]
        data_inicio = self.cleaned_data["data_inicio"]
        tipo_refeicao = self.cleaned_data["tipo_refeicao"]
        data_fim = self.cleaned_data["data_fim"]

        tipo_refeicao = Refeicao.objects.get(nome=self.cleaned_data["tipo_refeicao"])

        cardapios_restaurante = CardapioRestaurante.objects.filter(
            restaurante=restaurante,
            cardapio__refeicao=tipo_refeicao,
            data_oferecida__range=(data_inicio, data_fim),
        )

        capacidade_agendamentos_usada = sum(
            Agendamento.objects.filter(cardapio_agendado=cr).count()
            for cr in cardapios_restaurante
        )
        
        capacidade_total_agendamentos = sum(
            cr.cardapio.refeicao.limite_agendamentos for cr in cardapios_restaurante
        )

        if capacidade_total_agendamentos > 0:
            porcentagem_uso = (capacidade_agendamentos_usada / capacidade_total_agendamentos) * 100
        else:
            porcentagem_uso = 0
        capacidade_de_uso_porcentagem = round(porcentagem_uso, 2)

        refeicoes_agendadas = {}
        for cr in cardapios_restaurante:
            agendamentos = Agendamento.objects.filter(cardapio_agendado=cr).count()
            refeicao_nome = cr.cardapio.refeicao.nome
            if refeicao_nome in refeicoes_agendadas:
                refeicoes_agendadas[refeicao_nome] += agendamentos
            else:
                refeicoes_agendadas[refeicao_nome] = agendamentos

        refeicoes_mais_agendadas = sorted(refeicoes_agendadas.items(), key=lambda x: x[1], reverse=True)

        # print(f"Capacidade usada: {capacidade_agendamentos_usada}")
        # print(f"Capacidade total: {capacidade_total_agendamentos}")
        # print(f"Porcentagem de uso: {capacidade_de_uso_porcentagem}%")
        
        # print("Refeições mais agendadas:")
        # for refeicao, agendamentos in refeicoes_mais_agendadas:
        #     print(f"{refeicao}: {agendamentos} agendamentos")

        return capacidade_agendamentos_usada, capacidade_de_uso_porcentagem, refeicoes_mais_agendadas