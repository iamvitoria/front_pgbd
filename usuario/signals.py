
from usuario.models import Usuario
from financeiro.models import Carteira
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Usuario)
def criar_carteira(sender, instance, **kwargs):
    
    Carteira.objects.get_or_create(usuario=instance)