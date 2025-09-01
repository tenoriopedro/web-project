import re
from django import forms
from cart.models import BudgetRequest


class BudgetRequestModelForm(forms.ModelForm):

    class Meta:
        model = BudgetRequest
        fields = 'name', 'phone', 'email', 'message'
        labels = {
            'name': 'Seu nome*',
            'phone': 'Seu telefone*',
            'email': 'Seu email*',
            'message': 'Deixe sua mensagem(opcional)'
        }

    # Validation to the NAME field
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        # Just letters 
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", name):
            self.add_error('name', 'ERRO! Detectado caracteres inválidos.')

        return name