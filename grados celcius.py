# Solicitar al usuario el tipo de conversión
print("Elige el tipo de conversión:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Introduce tu opción (1 o 2): ")

# Realizar la conversión según la opción elegida
if opcion == '1':
    # Convertir de Celsius a Fahrenheit
    temp_celsius = float(input("Introduce la temperatura en Celsius: "))
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F")
elif opcion == '2':
    # Convertir de Fahrenheit a Celsius
    temp_fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    print(f"{temp_fahrenheit}°F equivalen a {temp_celsius:.2f}°C")
else:
    # Mensaje para opción inválida
    print("Opción no válida. Por favor, elige 1 o 2.")
