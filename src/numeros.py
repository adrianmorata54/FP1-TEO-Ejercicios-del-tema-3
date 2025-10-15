def invierte_numero(numero: int) -> int:
    resultado = 0
    while numero != 0:
        cifra = numero % 10
        resultado = resultado * 10 + cifra
        numero = numero // 10
    return resultado

def convierte_binario(numero: int) -> int:
    resultado = ''
    while not numero/2 == 0:
        resto = str(numero % 2)
        resultado = resto + resultado
        numero = numero//2
    if resultado == '':
        resultado += '0'
    return resultado

def sumar_divisores_propios(n: int) -> str:
    resultado = 0
    for i in range(1, n):
        if n % i == 0:
            resultado += i
    return resultado


def clasifica_numero(n: int) -> str:
    if n < sumar_divisores_propios(n):
        return 'Abundante'
    elif n == sumar_divisores_propios(n):
        return 'Perfecto'
    else:
        return 'Deficiente'


def clasifica_rango(n: int) -> str:
    resultado = ''
    for i in range(1, n+1):
        resultado = resultado + str(i) + ': ' + clasifica_numero(i) + '\n'
    return resultado

def busca_perfecto(n:int) -> str:
    contador = n
    numero = 1
    resultado = ''
    while contador != 0:
        if clasifica_numero(numero) == 'Perfecto':
            resultado += str(numero) + ' '
            contador -= 1
        numero +=1
    return resultado

