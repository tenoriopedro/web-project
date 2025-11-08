from django import forms
from .models import SobMedidaRequest
from utils.clean_functions import validate_letters_only, validate_phone
import re


class SobMedidaRequestModelForm(forms.ModelForm):

    class Meta:
        model = SobMedidaRequest

        fields = [
            'name', 'phone', 'email', 'project_description', 'attachment'
        ]

        labels = {
            'name': 'Seu Nome Completo*',
            'phone': 'Telefone/Whatsapp*',
            'email': 'Seu Melhor Email*',
            'project_description': 'Descreva seu projeto*',
            'attachment': 'Anexar planta ou desenho (Opcional)',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ex: João Silva'}),
            'phone': forms.TextInput(
                attrs={'placeholder': 'Ex: 21 999999999'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Ex: joao.silva@email.com'}
            ),
            'project_description': forms.Textarea(
                attrs={
                    'rows': 6,
                    'placeholder': 'Descreva o que você precisa.'
                }
            ),
            'attachment': forms.ClearableFileInput(
                attrs={
                    'accept': '.pdf, .jpg, .jpeg, .png'
                }
            ),
        }
        help_texts = {
            'attachment': 'Tipos aceitos: .pdf, .jpg, .png. Limite: 5MB'
        }

    def clean_name(self):
        return validate_letters_only(
            self.cleaned_data.get("name"),
            "name",
            self
        )

    def clean_phone(self):

        phone_data = self.cleaned_data.get("phone")

        if not phone_data:
            return phone_data

        sanitized_phone = re.sub(r'\D', '', phone_data)
        validate_phone(sanitized_phone, "phone", self)

        return sanitized_phone

    def clean_attachment(self):

        file = self.cleaned_data.get('attachment')

        if file:

            if file.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "O ficheiro é muito grande. O limite é 5MB."
                )

            valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
            extension = '.' + file.name.split('.')[-1].lower()

            if extension not in valid_extensions:
                raise forms.ValidationError(
                    "Tipo de ficheiro inválido. Apenas "
                    f"{', '.join(valid_extensions)} são aceitos."
                )

        return file
