def format_number(number):
    # Redondear el número a dos decimales y formatear como cadena
    return f"{number:.2f}"

# Ejemplos de uso
print(format_number(5.5589))  # Salida: '5.56'
print(format_number(3.3424))  # Salida: '3.34'
print(format_number(1))       # Salida: '1.00'
print(format_number(2.1))     # Salida: '2.10'