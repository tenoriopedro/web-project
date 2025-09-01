import re
from django import forms
from website.models import Contacts


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
    
    # Validação para o campo "NOME" no formulário
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        # Validação para receber apenas letras
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", first_name):
            self.add_error('first_name', 'ERRO! Detectado caracteres inválidos.')

        return first_name
    
    # Validação para o campo "SOBRENOME" no formulário
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        # Validação para receber apenas letras
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", last_name):
            self.add_error('last_name', 'ERRO! Detectado caracteres inválidos.')

        return last_name
    
    # Validação para o campo "MENSAGEM" no formulário
    def clean_message(self):
        message = self.cleaned_data.get('message')

        if len(message.strip()) < 10:
            self.add_error('message','ERRO! Mensagem muito curta.')

        return message