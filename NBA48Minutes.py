def nba_extrap(ppg, mpg):
    # Si minutos por juego es 0, devolver 0
    if mpg == 0:
        return 0

    # Calcular puntos por minuto
    ppg_per_minute = ppg / mpg

    # Extrapolar puntos para 48 minutos
    extrapolated_ppg = ppg_per_minute * 48

    # Redondear al decimal más cercano y devolver
    return round(extrapolated_ppg, 1)


# Ejemplos de uso
print(nba_extrap(12, 20))  # Salida: 28.8
print(nba_extrap(10, 10))  # Salida: 48
print(nba_extrap(5, 17))  # Salida: 14.1
print(nba_extrap(0, 0))  # Salida: 0