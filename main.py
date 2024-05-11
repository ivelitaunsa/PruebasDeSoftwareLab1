def clasificar_triangulo(lado1, lado2, lado3):
    """
    Esta función clasifica un triángulo según sus lados.
    Args:
    lado1: La longitud del primer lado.
    lado2: La longitud del segundo lado.
    lado3: La longitud del tercer lado.
    Returns:
    Un string que indica si el triángulo es escaleno,
    isósceles, equilátero o inválido.
    """

    #Se verifica que los valores ingresados no sea o sean 0 ni negativos
    if(lado1 <= 0 or lado2 <= 0 or lado3 <=0):
        if(lado1 == 0 or lado2 == 0 or lado3 ==0):
            return "El triángulo no puede tener un lado con valor 0"
        return "El triángulo no puede tener un lado negativo"

    # Verificar si el triángulo es válido, (Caso de prueba 5)
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "Triángulo inválido"
    # Clasificar el triángulo
    if lado1 == lado2 == lado3:
        return "Triángulo equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Triángulo isósceles"
    else:
        return "Triángulo escaleno"

# Solicitar al usuario la longitud de los lados
try: 
    # Se acepta un número lo suficientementegrande
    # Se verifica si se introduce varios numero por lado (Caso de prueba 9)
    lado1_input = input("Ingrese la longitud del primer lado: ")
    if len(lado1_input.split()) > 1:
        raise ValueError("El lado no puede contener más de un número.")
    lado1 = int(lado1_input)

    lado2_input = input("Ingrese la longitud del segundo lado: ")
    if len(lado2_input.split()) > 1:
        raise ValueError("El lado no puede contener más de un número.")
    lado2 = int(lado2_input)

    lado3_input = input("Ingrese la longitud del tercer lado: ")
    if len(lado3_input.split()) > 1:
        raise ValueError("El lado no puede contener más de un número.")
    lado3 = int(lado3_input)
    
except ValueError: # Excepcion contra caracterires diferentes a números (Caso de prueba 6) (Caso de prueba 7)
    print("Los lados del triángulo deben ser números positivos")    
    
except KeyboardInterrupt: # Excepcion por interrupcion del programa (Caso de prueba 8)
    print("\n\nInterrumpido por el usuario.")
    exit()
    

    
else:
    # Clasificar el triángulo y mostrar el resultado
    clasificacion = clasificar_triangulo(lado1, lado2, lado3)
    print(f"El triángulo es: {clasificacion}")
