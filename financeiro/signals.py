from django.db.models.signals import post_save
from django.dispatch import receiver
from financeiro.models import Transacao

@receiver(post_save, sender=Transacao)
def alterar_saldo_usuario(sender, instance, created, **kwargs):
    if created:
        if instance.is_entrada:
            instance.carteira.saldo += instance.valor
        else:
            instance.carteira.saldo -= instance.valor
        instance.carteira.save()
