from django import forms

class FormularioRecarga(forms.Form):
    valor_recarga = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Valor da Recarga",
        min_value=0.01,
    )
