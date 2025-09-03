import re


def validate_letters_only(value, field_name, form):
    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", value or ""):
        form.add_error(
            field_name, 
            'ERRO! Detectado caracteres inválidos.'
        )
    return value

def validate_phone(value, field_name, form):
    """
    Validates Brazilian cell phone numbers
    21 999999999
    """
    if not re.match(r"^\d{2}\s?9\d{8}$", value or ""):
        form.add_error(
            field_name,
            'ERRO! O telefone deve estar no formato: 21 999999999'
        )
        return value
    