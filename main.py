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

    # Verificar si el triángulo es válido
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
    lado1 = float(input("Ingrese la longitud del primer lado: "))
    lado2 = float(input("Ingrese la longitud del segundo lado: "))
    lado3 = float(input("Ingrese la longitud del tercer lado: "))
except ValueError:
    print("Los lados del triángulo deben ser números positivos")
else:
    # Clasificar el triángulo y mostrar el resultado
    clasificacion = clasificar_triangulo(lado1, lado2, lado3)
    print(f"El triángulo es: {clasificacion}")
