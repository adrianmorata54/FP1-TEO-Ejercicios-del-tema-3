# FP1-TEO-Ejercicios-del-tema-3


## Ejercicio 1: Invertir cadena

Implementa una función `invierte_cadena` en un módulo `cadenas.py` que reciba una cadena y devuelva la misma cadena invertida. Por ejemplo, si le pasamos `"Texto de prueba"` debe devolver `"abeurp ed otxeT"`. 

Implementa pruebas usando `assert` con estas cadenas de entrada: `""`, `"Texto de prueba"` y `"seres"`. Hazlo en un módulo llamado `cadenas_test.py`.

## Ejercicio 2: ¿Es palíndromo?

Implementa una función `es_palindromo` en el módulo `cadenas.py` que reciba una cadena y devuelva `True` si la cadena es un palíndromo y `False` en caso contrario. Un palíndromo es un texto que se lee igual de izquierda a derecha y de derecha a izquierda. Por ejemplo, la palabra `"reconocer"` es un palíndromo.

Incluye dos parámetros opcionales, además de la cadena:
* `ignora_espacios`:  de tipo `bool`, si es `True` no se tendrán en cuenta los espacios. Por ejemplo, `"yo hago yoga hoy"` será considerado palíndromo si el pámetro es `True`. 
* `ignora_mayusculas`: de tipo `bool`, si es `True` no se tendrán en cuenta las mayúsculas. Por ejemplo, `"Ana"` será considerado un palíndromo si el parámetro es `True`. 

Implementa pruebas usando `assert` con distintos parámetros de entrada. Aquí tienes algunos palíndromos de ejemplo: 

``` 
reconocer
rotor
radar
Amor a Roma
Luz azul
``` 

Hazlo en el módulo `cadenas_test.py`.

## Ejercicio 3: Estilizador de mensajes

Implementa una función `estiliza_mensaje` que recibe una cadena y permite obtener otra con algunos cambios estéticos. Los cambios a realizar se pueden controlar mediante diversos parámetros opcionales:

* `alterna_may_min`: de tipo `bool`, por defecto `True`. Hace que se intercalen letras mayúsculas y minúsculas. Por ejemplo, el texto `"Fundamentos de programación 1"` quedaría como `"FuNdAmEnToS dE pRoGrAmAcIóN 1"`. Observa que no se tienen en cuenta los caracteres que no son letras se dejan tal como están, y no cuentan para ir alternando entre mayúsculas y minúscula. 
* `usa_dieresis`: de tipo `bool`, por defecto `False`. Permite añadir una diéresis a todas las vocales que no incluyan tildes. Por ejemplo, `"Murciélago"` quedaría como `"Mürcïélägö". 
* `sustituye_espacios`: de tipo `str`, por defecto `" "`. Se utiliza la cadena indicada para sustituir cada uno de los espacios de la cadena de entrada. Por ejemplo, si `sustituye_espacios` es `"*"`, la cadena de entrada `"Soy un programador experto"` se transforma en `"Soy*un*programador*experto"`.

Las pruebas para esta función se proporcionan ya implementadas en el módulo `cadenas_test.py`. 

## Ejercicio 4: Cifrado César

Implementa una función `cifra_cesar` en un módulo `codificacion.py` que codifique un mensaje utilizando el Cifrado César Básico:

* Consiste en reemplazar cada letra con la letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.
* Usaremos como alfabeto el siguiente: `"abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"` 
* Diremos que este número fijo que vamos a usar para los incrementos de las letras es la **clave**. Así por ejemplo, para una clave 3, la letra `A` se convertirá en `D`. 
* Haremos este incremento de manera circular, de manera que para la misma clave anterior la letra `Ü` se convertiría en `c`. 
* Sólo deben codificarse las letras que aparecen en el alfabeto anterior; el resto de caracteres se dejará tal cual estén en el mensaje de entrada. 

La función va a recibir dos parámetros, uno con el texto a codificar, y otro con la clave (un número entero), y devolverá el mensaje codificado. 

Para poder "sumar" un número de posiciones a una letra dada, implemente estas dos funciones antes de implementar `cifra_cesar`:

* `def letra_a_posicion(letra)`: Convierte una letra en su posición dentro del alfabeto. Si el carácter no es una letra, devuelve `None`.
* `def posicion_a_letra(posicion)`: Convierte una posición en la letra correspondiente del alfabeto. Si la posición está fuera de rango, devuelve `None`.

En los siguiente ejemplos se muestra la salida esperada de `cifra_cesar` para distintos casos de prueba:

```
>>> cifra_cesar("Hola Mundo", 1)
"Ipmb Nvñep"
>>> cifra_cesar("Hola Mundo", 13)
"Téxn YBzpé"
>>> cifra_cesar("Hola Mundo", 66)
"Hola Mundo"
```

Implementa pruebas usando `assert` para estos casos de prueba. Hazlo en un módulo llamado `codificacion_test.py`.

## Ejercicio 5: Hackeando el cifrado César

Queremos hackear un mensaje codificado con el cifrado César. Dado que hay muy pocas claves posibles (tantas como letras en el alfabeto menos uno), vamos a probarlas todas y mostrar el resultado al usuario para que decida. 

Implementa una función `rompe_cesar` que reciba un mensaje cifrado y muestre al usuario el resultado de decodificar el mensaje para cada uno de los desplazamientos posibles (claves). Ten en cuenta que puedes usar la misma función `cifra_cesar` con la clave en negativo para decodificar un mensaje cifrado. 

Utiliza la función para adivinar el siguiente mensaje: `"j YÁXOÁJUJÁ ÉN JYÁNVMN yáxoájujvmx!"`. 

## Ejercicio 6: Invierte número entero

En el módulo `numeros.py`, implementa una función `invierte_numero` que recibe un número entero como parámetro y devuelve el número resultante de invertir sus dígitos. Ten en cuenta las siguientes pistas:
* Para extraer la última cifra de un número, utiliza la operación "resto entre 10".
* Para eliminar la última cifra de un número, utiliza la operación "cociente entre 10".
* Para añadir una cifra en última posición a un número, multiplica el número por 10 y súmale la cifra.

Con estas pistas, implementa un bucle `while` que resuelva el problema.

Utiliza la función `test_invierte_numero` del módulo `numeros_test.py` para probar tu implementación.

## Ejercicio 7: Conversión a binario

En el módulo `numeros.py`, implementa una función `convierte_binario` que reciba un número entero decimal (base 10) y devuelve una cadena de texto con su representación binaria (base 2). Este es un concepto fundamental en la informática.

Utiliza el método de la división sucesiva por 2, que se muestra a continuación con un ejemplo:

| Entrada (Decimal) | Proceso (División) | Resto | Binario (Construcción Inversa) | Salida Esperada |
| :---: | :---: | :---: | :---: | :---: |
| **13** | $13/2 = 6$ | **1** | "1" | "1101" |
| | $6/2 = 3$ | **0** | "01" | |
| | $3/2 = 1$ | **1** | "101" | |
| | $1/2 = 0$ | **1** | "1101" | |


Utiliza la función `test_convierte_binario` del módulo `numeros_test.py` para probar tu implementación.

## Ejercicio 8: Clasificador de Números Perfectos, Abundantes y Deficientes

Queremos implementar una función `clasifica_rango` que clasifique los números enteros positivos menores a `n` en tres categorías:

* **Número perfecto**: es aquel que es igual a la suma de sus divisores propios. Por ejemplo, el $6$ (ya que $1 + 2 + 3 = 6$).
* **Número abundante**: es aquel que es menor a la suma de sus divisores propios. por ejemplo, el $12$ (ya que $1 + 2 + 3 + 4 + 6 = 16$).
* **Número deficiente**: es aquel que es mayor a la suma de sus divisores propios. por ejemplo, el $10$ (ya que $1 + 2 + 5 = 8$).

Resuelve este problema implementando las siguientes funciones en el módulo `numeros.py`:

* Función `sumar_divisores_propios`: recibe un número entero `n` y calcula la suma de todos sus divisores positivos, excluyendo a sí mismo. 
* Función `clasifica_numero`: recibe un número entero `n` y devuelve la clasificación del número como una cadena de texto (`"Perfecto"`, `"Abundante"` o `"Deficiente"`). 
* Función `clasifica_rango`: recibe un número entero `n` y muestra por pantalla la clasificación de todos los números en el intervalo $[1, n]$.

La salida por pantalla para la llamada `clasifica_rango(20)` debe ser parecida a esta:

```
1: Deficiente
2: Deficiente
3: Deficiente
4: Deficiente
5: Deficiente
6: Perfecto
7: Deficiente
8: Deficiente
9: Deficiente
10: Deficiente
11: Deficiente
12: Abundante
13: Deficiente
14: Deficiente
15: Deficiente
16: Deficiente
17: Deficiente
18: Abundante
19: Deficiente
20: Abundante
```

Por último, implementa una función `busca_perfecto` que reciba un número entero `n` y devuelva el número perfecto n-ésimo. Por ejemplo, si invocamos a `busca_perfecto(1)`, devolvería `6`. 

Ejecuta la función `test_busca_perfecto` del módulo `numeros_test.py` para probar la función. 


## Ejercicio 9: Planificación de Eventos Recurrentes

Queremos planificar una serie de **eventos recurrentes** con un **intervalo fijo** de días entre ellos, asegurándonos de que cada evento caiga en un **día laborable**. Un día se considera **no laborable** si es fin de semana (sábado o domingo) o un día festivo. Si una fecha calculada para un evento cae en un día no laborable, la fecha debe **retrasarse** al siguiente día laborable.

Para resolver este problema, se te proporciona una función auxiliar `es_dia_festivo(fecha: date) -> bool` que verifica si una fecha es un día festivo (simulando un calendario de días festivos predefinido). **Esta función se da implementada** en el módulo `eventos.py` y no debes modificarla.

Deberás implementar las siguientes funciones en el módulo `eventos.py`:


* Función `es_dia_no_laborable`: Recibe una fecha y devuelve `True` si es fin de semana (sábado o domingo) o si es un día festivo (utilizando la función `es_dia_festivo`). Devuelve `False` en caso contrario.

* Función `calcular_siguiente_valida`: Recibe la fecha de la última ocurrencia (`fecha_anterior`) y un intervalo en días (número entero `intervalo_dias`). Calcula la próxima fecha sumando el intervalo. Si la fecha resultante cae en un día no laborable, la función debe **avanzar día a día** hasta encontrar el siguiente día laborable, devolviendo esta fecha.

* Función `planificar_eventos`: Recibe una `fecha_inicio` para los eventos, un `intervalo_dias` (días entre cada dos eventos)  y el número de eventos en total a planificar (número entero `num_eventos`). Genera y muestra por pantalla las fechas para cada uno de los eventos. Ten en cuenta que:
    * La planificación comienza con `fecha_inicio`. **Importante**: si `fecha_inicio` cae en un día no laborable, se debe ajustar al siguiente día laborable antes de contarla como el primer evento.
    * A partir de la primera fecha válida, cada evento subsiguiente se calcula utilizando la función `calcular_siguiente_valida`.
    * El formato de salida debe ser: `"Evento X: YYYY-MM-DD"`.


#### Pruebas

Implementa las funciones de prueba necesarias en el módulo `eventos_test.py` usando `assert` para verificar el correcto funcionamiento de:
* `es_dia_no_laborable`: Prueba casos que incluyan: un día de semana laborable, un fin de semana (sábado o domingo) y un día festivo.
* `calcular_siguiente_valida`: Prueba al menos dos casos, uno en el que la fecha siguiente sea laborable, y otro caso donde la fecha siguiente calculada (sumando el intervalo) caiga en un día **no laborable** y deba ser ajustada al siguiente día laborable.

Incluye también una llamada a la función `planificar_eventos`, pasándole estos valores en los parámetros:

* `fecha_inicio = date(2026, 1, 1)` (corresponde a un día festivo)
* `intervalo_dias = 10`
* `num_eventos = 5`

La salida por pantalla debe ser:
```
--- Planificación de 5 eventos recurrentes (Intervalo: 10 días) ---
Evento 1: 2026-01-02
Evento 2: 2026-01-12
Evento 3: 2026-01-22
Evento 4: 2026-02-02
Evento 5: 2026-02-12
```

Ejecuta estas pruebas para confirmar que las implementaciones son correctas.