def total_pressure(M1, M2, m1, m2, V, T):
    # Constante de los gases en atm·L·K⁻¹·mol⁻¹
    R = 0.0821

    # Convertir la temperatura de Celsius a Kelvin
    T_K = T + 273.15

    # Calcular los moles de cada gas
    n1 = m1 / M1
    n2 = m2 / M2

    # Calcular la presión total usando la ecuación de los gases ideales
    P_total = (n1 + n2) * R * T_K / V

    return P_total


# Ejemplos de uso
print(total_pressure(28, 44, 10, 20, 2, 25))  # Ejemplo con valores arbitrarios