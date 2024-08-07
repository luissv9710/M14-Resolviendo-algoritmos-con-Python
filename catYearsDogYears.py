def convert_years(humanYears):
    if humanYears < 1 or not isinstance(humanYears, int):
        raise ValueError("Los años humanos deben ser un número entero mayor o igual a 1.")

    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Ejemplo de uso

result = convert_years(1)
print(result)
result = convert_years(2)
print(result)
result = convert_years(3)
print(result)
result = convert_years(11)
print(result)  # Salida: [5, 32, 39]
