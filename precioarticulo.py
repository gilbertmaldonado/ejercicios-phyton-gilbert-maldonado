# Pedir al usuario el precio del artículo
precio_articulo = float(input("Ingrese el precio del artículo: "))

# Pedir al usuario la cantidad de unidades
cantidad_unidades = int(input("Ingrese la cantidad de unidades que desea comprar: "))

# Calcular el costo total
costo_total = precio_articulo * cantidad_unidades

# Imprimir el mensaje con el costo total
print(f"El costo total de su compra es: {costo_total} pesos.")
