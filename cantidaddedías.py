# Pedir al usuario la cantidad de días
cantidad_dias = int(input("Ingresa un número entero de días: "))

# Calcular las horas
cantidad_horas = cantidad_dias * 24

# Calcular los minutos
cantidad_minutos = cantidad_horas * 60

# Imprimir el resultado
print(f"{cantidad_dias} días equivalen a {cantidad_horas} horas o {cantidad_minutos} minutos.")
