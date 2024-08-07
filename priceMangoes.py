def mango(quantity, price):
    # Calcula cuántos mangos se pagan (2 por cada 3)
    paid_mango_count = (quantity // 3) * 2 + (quantity % 3)
    # Calcula el costo total
    total_cost = paid_mango_count * price
    return total_cost

# Ejemplos de uso
print(mango(2, 3))  # Salida: 6
print(mango(3, 3))  # Salida: 6
print(mango(5, 3))  # Salida: 12
print(mango(9, 5))  # Salida: 30