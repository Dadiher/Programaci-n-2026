# Problema #4: Validador de compra con descuento (Versión sencilla)

# Entrada
precio = float(input("Digite el precio del producto: "))

# Proceso: Si el precio es 50000 o más, se le aplica un 15% de descuento
if precio >= 50000:
    descuento = precio * 0.15
    precio_final = precio - descuento
    mensaje = "¡Aplica para el 15% de descuento!"
else:
    precio_final = precio
    mensaje = "No aplica para descuento."

# Salida esperada
print("-" * 50, "\n")
print(mensaje)
print(f"Total a pagar: ₡{precio_final}")