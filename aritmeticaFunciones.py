# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números (con control de división entre cero)
def dividir(a, b):
    if b == 0:
        return "Error: división entre cero"
    return a / b

# Función para calcular el cuadrado de un número
def cuadrado(x):
    return x ** 2

# Función para calcular el cubo de un número
def cubo(x):
    return x ** 3

# Función para calcular el valor absoluto de un número
def valor_absoluto(x):
    return -x if x < 0 else x

# Ejemplos de uso
print("Suma:", sumar(5, 3))
print("Resta:", restar(5, 3))
print("Multiplicación:", multiplicar(5, 3))
print("División:", dividir(5, 0))
print("Cuadrado:", cuadrado(4))
print("Cubo:", cubo(2))
print("Valor absoluto:", valor_absoluto(-7))
