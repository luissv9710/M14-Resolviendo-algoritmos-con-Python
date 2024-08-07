import math

def adjust_to_16_9(x, y):
    # Calculamos el nuevo ancho manteniendo la altura igual
    new_width = math.ceil(y * (16 / 9))
    return new_width

# Ejemplo de uso
x = 374
y = 280
print(adjust_to_16_9(x, y))  # Salida esperada: 498