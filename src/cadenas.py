def invierte_cadena(texto: str):
    '''
    Recibe una cadena de texto y devuelve la misma invertida
    '''
    resultado = ''
    for caracter in texto:
        resultado = caracter + resultado
    return resultado

def es_palindromo(cadena: str, ignora_espacios: bool, ignora_mayusculas: bool) -> bool:
    if ignora_espacios:
        cadena = cadena.replace(' ', '')
    if ignora_mayusculas:
        cadena = cadena.upper()
    inversa = invierte_cadena(cadena)
    return inversa == cadena

def estiliza_mensaje(cadena: str, alterna_may_min: bool = True, usa_dieresis: bool = False, sustituye_espacios: str = ' ') -> str:
    resultado= ''
    posición_par = True
    vocales = {'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü',
               'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü'}
    for c in cadena:
        if c == ' ':
            resultado += sustituye_espacios
        elif alterna_may_min and c.isalpha():
            if usa_dieresis and c in vocales:
                c = vocales[c]
            if posición_par:
                resultado += c.upper()
                posición_par = False
            elif not posición_par:
                resultado += c.lower()
                posición_par = True
        else:
            if usa_dieresis and c in vocales:
                resultado += vocales[c]
            else:
                resultado += c
              
    return resultado
