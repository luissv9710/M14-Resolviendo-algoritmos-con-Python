def convert_usd_to_cny(usd_amount):
    # Tipo de cambio de USD a CNY
    conversion_rate = 6.75
    # Convertir USD a CNY
    cny_amount = usd_amount * conversion_rate
    # Formatear el resultado a dos decimales y construir la cadena de salida
    return f"{cny_amount:.2f} Chinese Yuan"

# Ejemplos de uso
print(convert_usd_to_cny(15))   # Salida: '101.25 Chinese Yuan'
print(convert_usd_to_cny(465))  # Salida: '3138.75 Chinese Yuan'