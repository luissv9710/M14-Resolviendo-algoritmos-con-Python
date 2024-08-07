import math

def calculate_litres(time):
    # Calcular los litros totales
    litres = time * 0.5
    # Redondear hacia abajo y devolver el resultado
    return math.floor(litres)

# Ejemplos de uso
print(calculate_litres(3))    # Salida: 1
print(calculate_litres(6.7))  # Salida: 3
print(calculate_litres(11.8)) # Salida: 5