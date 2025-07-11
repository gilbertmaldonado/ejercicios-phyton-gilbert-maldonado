# Solicitar al usuario su peso en kilogramos
peso_kg = float(input("Por favor, introduce tu peso en kilogramos (ej. 70.5): "))

# Solicitar al usuario su altura en metros
altura_m = float(input("Ahora, introduce tu altura en metros (ej. 1.75): "))

# Calcular el IMC
# La fórmula es peso / (altura al cuadrado)
imc = peso_kg / (altura_m ** 2)

# Imprimir el resultado del IMC
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
