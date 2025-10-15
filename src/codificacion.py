def letra_a_posicion(letra: str, lista: str) -> int:
    if not letra.isalpha():
        return None
    else:
        return lista.find(letra)

def posicion_a_letra(posicion: int, lista: str) -> str:
    if posicion >= len(lista):
        return None
    else:
        return lista[posicion]




def cifra_cesar(frase: str, clave: int) -> str:
    resultado = ''
    alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    for letra in frase:
        if letra in alfabeto:
            posicion = letra_a_posicion(letra, alfabeto)
            nueva_posicion = (posicion + clave) % len(alfabeto)
            resultado +=posicion_a_letra(nueva_posicion, alfabeto)
        else:
            resultado += letra
    return resultado
        

def rompe_cesar(frase: str) -> str:
    resultados = ''
    alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    for clave in range(len(alfabeto)):
        resultado = ''
        for letra in frase:
            if letra in alfabeto:
                posicion = letra_a_posicion(letra, alfabeto)
                nueva_posicion = (posicion - clave) % len(alfabeto)
                resultado +=posicion_a_letra(nueva_posicion, alfabeto)
            else:
                resultado += letra
        resultados += f'Clave {clave}: {resultado}\n'
    return resultados
print(rompe_cesar("j YÁXOÁJUJÁ ÉN JYÁNVMN yáxoájujvmx!"))