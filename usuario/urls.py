from django.urls import path
from usuario.views import logar_usuario, cadastrar, esqueci_senha, definir_preferencias_alimentares, index, logout_view

urlpatterns = [
    path("login/", logar_usuario, name='login'),
    path("cadastrar/", cadastrar, name='cadastrar'),
    path("esqueci-senha/", esqueci_senha, name='esqueci-senha'),
    path("preferencias-alimentares/", definir_preferencias_alimentares, name='preferencias-alimentares'),
    path("", index, name='index'),
    path("logout/", logout_view, name='logout'),
]
