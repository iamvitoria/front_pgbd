from django.db.models.signals import post_save
from django.dispatch import receiver
from usuario.models import Preferencias
from .models import CardapioRestaurante

@receiver(post_save, sender=CardapioRestaurante)
def avisar_alunos_comida_favorita_no_cardapio(sender, instance, created, **kwargs):
    if created:
        preferencias = Preferencias.objects.all()
        for pref in preferencias:
            comidas_favs = pref.comidas_favoritas.split(',') if ',' in pref.comidas_favoritas else [pref.comidas_favoritas]

            for comida_fav in comidas_favs:
                if comida_fav.strip() in instance.cardapio.refeicao.nome:
                    print(f"Enviando notificação para {pref.usuario.nome_completo} sobre a comida favorita no cardápio")

@receiver(post_save, sender=CardapioRestaurante)
def verificar_quantia_agendamentos_dia_limite_para_restaurante(sender, instance, created, **kwargs):

    if created:
        cardapios = CardapioRestaurante.objects.filter(
            data_oferecida=instance.data_oferecida,
            restaurante=instance.restaurante
        )

        if cardapios.count() > instance.cardapio.refeicao.limite_agendamentos:
            print(f"Enviando notificação para o restaurante {instance.restaurante.nome} sobre a quantidade de agendamentos no dia limite")