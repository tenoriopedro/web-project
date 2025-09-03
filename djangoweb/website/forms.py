from django import forms
from website.models import Contacts
from utils.clean_functions import validate_letters_only


class ContactsModelForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = 'first_name', 'last_name', 'email', 'message',
        labels = {
            'first_name': 'Seu nome*',
            'last_name': 'Seu sobrenome*',
            'email': 'Seu email*',
            'message': 'Sua mensagem*',
        }
    
    # Validation for the "NOME" field in the form
    def clean_first_name(self):
        return validate_letters_only(
            self.cleaned_data.get("first_name"),
            "first_name",
            self
        )
    
    # Validation for the "SOBRENOME" field in the form
    def clean_last_name(self):
        return validate_letters_only(
            self.cleaned_data.get("last_name"),
            "last_name",
            self
        )
    
    # Validação para o campo "MENSAGEM" no formulário
    def clean_message(self):
        message = self.cleaned_data.get('message')

        if len(message.strip()) < 10:
            self.add_error('message','ERRO! Mensagem muito curta.')

        return message