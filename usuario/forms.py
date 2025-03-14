# forms.py
from django import forms
from .models import Usuario, Preferencias


class UsuarioCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'cpf', 'telefone', 'data_nascimento', 'imagem']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('As senhas não coincidem.')

        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user

class PreferenciasForm(forms.ModelForm):
    class Meta:
        model = Preferencias
        fields = ["comidas_favoritas", "vegetariano", "onivoro"]
        labels = {
            "comidas_favoritas": "comidas favoritas",
            "vegetariano": "vegeteriano",
            "onivoro": "onivora",
        }
        widgets = {
            "comidas_favoritas": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "vegetariano": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "onivoro": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        vegetariano = cleaned_data.get("vegetariano")
        onivoro = cleaned_data.get("onivoro")

        if not (vegetariano or onivoro):
            raise forms.ValidationError(
                "At least one dietary preference (vegetarian or omnivore) must be selected."
            )
        if vegetariano and onivoro:
            raise forms.ValidationError(
                "Both vegetarian and omnivore cannot be selected at the same time."
            )
        return cleaned_data
