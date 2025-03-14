from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Agendamento


@receiver(post_save, sender=Agendamento)
def gerenciar_fila_espera(sender, instance, created, **kwargs):
    if created:
        restaurante_limite = instance.cardapio_agendado.cardapio.refeicao.limite_agendamentos
        agendamentos_count = Agendamento.objects.filter(
            cardapio_agendado=instance.cardapio_agendado
        ).count()

        if agendamentos_count > restaurante_limite:
            instance.is_fila_espera = True
            instance.posicao_fila = agendamentos_count - restaurante_limite
            print(
                f"Colocando {instance.usuario.nome_completo} na fila de espera do restaurante {instance.restaurante.nome}")
        else:
            instance.is_fila_espera = False
            instance.posicao_fila = 0

        instance.save()

    else:
        try:
            previous_instance = Agendamento.objects.get(id=instance.id)
            checkin_changed = previous_instance.checkin != instance.checkin
            fila_espera_changed = previous_instance.is_fila_espera != instance.is_fila_espera

            if checkin_changed:
                if instance.checkin:
                    print(f"{instance.usuario.nome_completo} realizou check-in.")
                    instance.is_fila_espera = False
                    instance.posicao_fila = 0
                    instance.save()

                    fila_espera = Agendamento.objects.filter(
                        cardapio_agendado=instance.cardapio_agendado,
                        is_fila_espera=True,
                        checkin=False
                    ).order_by('data_agendamento')

                    for posicao, item in enumerate(fila_espera, start=1):
                        item.posicao_fila = posicao
                        item.save()

                else:
                    print(f"{instance.usuario.nome_completo} cancelou o check-in.")

            if fila_espera_changed:
                print(
                    f"O status da fila de espera para {instance.usuario.nome_completo} mudou para {instance.is_fila_espera}.")

        except Agendamento.DoesNotExist:
            print("Agendamento não encontrado ao atualizar.")