from django.urls import path
from cardapio.views import ver_cardapio, ver_cardapio_semana, selecionar_restaurante

urlpatterns = [
    path("ver/<int:restaurante_id>", ver_cardapio, name='ver_cardapio'),
    path("ver/semana/<int:restaurante_id>", ver_cardapio_semana, name='ver_cardapio_semana'),
    path("selecionar_restaurante", selecionar_restaurante, name='selecionar_restaurante_cardapio')
]
