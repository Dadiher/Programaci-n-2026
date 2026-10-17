# Problema #2: Detector de número par/impar

# Entrada
try:
    numero = int(input("Digite un número entero: "))
    
    # Proceso y Salida esperada
    if numero % 2 == 0:
        resultado = f"El número {numero} es PAR."
    else:
        resultado = f"El número {numero} es IMPAR."
        
    print("-" * 50, '\n')
    print(resultado)

except ValueError:
    print("-" * 50, '\n')
    print("Error: Debe digitar un número entero válido.")
    
    