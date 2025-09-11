from django import forms
from cart.models import BudgetRequest
from utils.clean_functions import validate_letters_only, validate_phone


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

    def clean_name(self):
        return validate_letters_only(
            self.cleaned_data.get("name"),
            "name",
            self
        )

    def clean_phone(self):
        return validate_phone(
            self.cleaned_data.get("phone"),
            "phone",
            self
        )
