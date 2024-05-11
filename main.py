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
# lado1 = int(input("Ingrese la longitud del primer lado: "))
# lado2 = int(input("Ingrese la longitud del segundo lado: "))
# lado3 = int(input("Ingrese la longitud del tercer lado: "))

# print(clasificar_triangulo(lado1, lado2, lado3))

# Clasificar el triángulo y mostrar el resultado
# clasificacion = clasificar_triangulo(lado1, lado2, lado3)
# print(f"El triángulo es: {clasificacion}")

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
# lado1 = int(input("Ingrese la longitud del primer lado: "))
# lado2 = int(input("Ingrese la longitud del segundo lado: "))
# lado3 = int(input("Ingrese la longitud del tercer lado: "))

# print(clasificar_triangulo(lado1, lado2, lado3))

# Clasificar el triángulo y mostrar el resultado
# clasificacion = clasificar_triangulo(lado1, lado2, lado3)
# print(f"El triángulo es: {clasificacion}")

# Caso de Prueba 1

# Caso de Prueba 2

# Caso de Prueba 3

# Caso de Prueba 4

# Caso de Prueba 5

# Caso de Prueba 6

# Caso de Prueba 7

# Caso de Prueba 8

# Caso de Prueba 9

# Caso de Prueba 10

# Caso de Prueba 11

# Caso de Prueba 12

# Caso de Prueba 13

# Caso de Prueba 14
