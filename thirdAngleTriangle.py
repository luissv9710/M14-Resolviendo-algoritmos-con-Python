def find_third_angle(angle1, angle2):
    # La suma de los ángulos interiores de un triángulo es 180 grados
    return 180 - (angle1 + angle2)

# Ejemplos de uso
print(find_third_angle(60, 90))  # Salida: 30
print(find_third_angle(45, 45))  # Salida: 90