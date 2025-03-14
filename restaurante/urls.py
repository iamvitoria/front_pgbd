from .views import definir_limite_agendamentos, verificar_agendamentos_semana, associar_cardapio_ao_restaurante, gerar_relatorios, ver_refeicoes
from django.urls import path

urlpatterns = [
    path("definir_limite_agendamentos/<int:refeicao_id>/", definir_limite_agendamentos, name='definir_limite_agendamentos'),
    path("ver_agendamentos_semana/<int:restaurante_id>/", verificar_agendamentos_semana, name='ver_agendamentos_semana'),
    path("associar_cardapio/", associar_cardapio_ao_restaurante, name='associar_cardapio'),
    path("gerar_relatorios/", gerar_relatorios, name='gerar_relatorios'),
    path("ver_refeicoes/", ver_refeicoes, name='ver_refeicoes'),
]