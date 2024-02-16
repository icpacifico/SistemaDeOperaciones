def validate_positive_integer(value):
    if value < 0:
        raise ValidationError('El valor debe ser un número positivo mayor o igual a 0.')