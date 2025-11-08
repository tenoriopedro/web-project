import re


def validate_letters_only(value, field_name, form):
    if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", value or ""):
        form.add_error(
            field_name,
            'ERRO! Detectado caracteres inválidos.'
        )
    return value


def validate_phone(value, field_name, form):

    if not value:
        return value

    if not re.match(r"^\d{2}9\d{8}$", value):
        form.add_error(
            field_name,
            'Telefone inválido. O formato deve ser (XX) 9XXXX-XXXX.'
        )

    return value
