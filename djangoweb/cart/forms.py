import re
from django import forms
from cart.models import BudgetRequest


class BudgetRequestModelForm(forms.ModelForm):

    class Meta:
        model = BudgetRequest
        fields = 'name', 'phone', 'email', 'message'
        labels = {
            'name': 'Nome*(Ex: João Silva)',
            'phone': 'Telefone*(Ex: 21 999999999)',
            'email': 'Seu email*',
            'message': 'Deixe sua mensagem(opcional)'
        }

    # Validation to the NAME field
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        # Just letters 
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", name):
            self.add_error(
                'name', 
                'ERRO! Detectado caracteres inválidos.'
            )

        return name
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        # Just numbers
        if not re.match(r"^\d{2}\s?9\d{8}$", phone):
            self.add_error(
                'phone', 
                'ERRO! O telefone deve estar no formato: 21 999999999'
            )

        return phone