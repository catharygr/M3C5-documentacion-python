## ¿Qué es un condicional?

Una condición en Python es una estructura que permite que el programa tome decisiones.
Evalúa una expresión que puede ser verdadera (`True`) o falsa (`False`), y dependiendo del resultado, ejecuta un bloque de código determinado. Para esto se utilizan las sentencias de control de flujo: `if, elif, else`. En otras palabras, permite que el programa responda de manera diferente según la situación.

Importante: Las condicionales utilizan operadores de comparación, los más comunes son:

```python
== # igual a
!= # no igual a
> # mayor que
< # menor que
>= # mayor o igual que
<= # menor o igual que
```

### Ejemplos:

#### Utilizando palabra de control de flujo: `if`

Condición expresada con lenguaje natural: **_Si tu edad es mayor o igual a 18, puedes acceder a una discoteca_**

```python
edad = 18
if edad >= 18:
  print("Eres mayor de edad")
```

#### Utilizando palabras de control de flujo: `if, else`

Condición expresada con lenguaje natural: **_Si tu edad es mayor o igual a 18, puedes acceder a una discoteca, en cualquier otro caso, no, porque eres menor de edad._**

```python
edad = 18
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
```

#### Utilizando palabras de control de flujo: `if, elif, else`

Condición expresada con lenguaje natural: **_Si tu edad es mayor e igual a 18, o menor e igual a 68, puedes optar por el puesto de trabajo._**

```python
edad = 18
if edad < 18:
  print("Eres menor de edad")
elif edad >= 68:
  print("Eres pensionista")
else:
  print("Puedes trabajar")
```

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Un bucle es una estructura que permite ejecutar un bloque de código varias veces sin tener que escribirlo repetidamente. Son útiles cuando, por ejemplo, necesitamos repetir algo hasta que se cumpla una condición, automatizar tareas repetitivas o procesar grandes cantidades de datos. Se pueden usar, entre otros tipos de datos, en las cadenas, listas, etc... Sin bucles, tendríamos que escribir muchas veces el mismo código, lo que sería poco eficiente y difícil de mantener.

### Tipo de bucles `for`

El bucle `for` se usa cuando sabemos cuántas veces queremos repetir algo o cuando queremos recorrer una colección de datos (lista, tupla, cadena, etc.).

Condición expresada con lenguaje natural: **_Recorre la lista `personas` y por cada `persona` la imprime en la consola._**

```python
personas = ["Caty", "Sasa", "Clau", "Carlos - el profe"]

for persona in personas:
    print(persona)
```

### Tipo de bucles `while`

El bucle `while` se usa cuando queremos que el código se repita mientras una condición sea verdadera.

Condición expresada con lenguaje natural: **_Mientras el `contador` es menor de 5 imprime el valor del contador, luego aumenta su valor actual por 1. Una vez que el `contador` llegue a 5, la condición retornará `False` y se sale del loop._**

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

### Control del flujo dentro de un bucle

Tenemos dos tipos de palabras clave para control de comportamiento de un bucle.

#### Palabra `continue`

Salta a la siguiente iteración del bucle sin ejecutar el resto del código. Suele estar acompañado con alguna condición.

Condición expresada con lenguaje natural: **_Iterar por el bucle imprimiendo el valor del elemento `numero`, si el número es igual a 2, no se imprimirá y el bucle seguirá con el siguiente elemento_**

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero == 2:
        continue
    print(numero)
```

#### Palabra `break`

Termina el bucle entero inmediatamente sin ejecutar el resto del código.

Condición expresada con lenguaje natural: **_Itera por los números e imprime su valor. Si el valor del número es igual a 3, sale del loop inmediatamente y deja de ejecutarlo._**

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero == 3:
        break
    print(numero)
```

### Importante

Es muy importante estar muy atentos a todas las condiciones en los bucles porque si nos equivocamos podríamos entrar en el llamado bucle infinito y esto puede hasta bloquear el ordenador del usuario, obligándolo no solo a cerrar la aplicación sino a reiniciarlo por completo.

## ¿Qué es una lista por comprensión en Python?

Es una forma sencilla y compacta de crear listas en Python usando una sola línea de código. Ayuda a generar listas aplicando una expresión a cada elemento de una secuencia y, opcionalmente, filtrando elementos con una condición.

Condición expresada con lenguaje natural: **_Crea una nueva lista `potencias` iterando por la lista `numeros` y retorna por cada `num` su potencia._**

```python
numeros = [1, 2, 3, 4, 5]

potencias = [num ** num for num in numeros]
```

#### Con la condición opcional:

Condición expresada con lenguaje natural: **_Crea una nueva lista `potencias` iterando por la lista `numeros` y retorna por cada `num` su potencia si se trata de un número par._**

```python
numeros = [1, 2, 3, 4, 5]

potencias = [num ** num for num in numeros if num % 2 == 0]
```

## ¿Qué es un argumento en Python?

Es el valor que se le pasa a una función cuando la llamamos para que pueda trabajar con él. En otras palabras, es el valor real que enviamos cuando usamos la función. Por otro lado, tenemos el parámetro que es la variable declarada en la definición de la función que recoge el argumento en el momento de su ejecución.

```python
def saludar(nombre): # "nombre" es un parámetro
    print("Hola", nombre)

saludar("Ana") # "Ana" es el argumento
```

## ¿Qué es una función Lambda en Python?

Son funciones en lineas y pueden ser anónimas porque no necesita un nombre, aunque se le puede asignar uno si queremos reutilizarla. Son muy útiles cuando queremos funciones rápidas y simples. Recibe parámetros y retorna la expresión.

Condición expresada con lenguaje natural: **_Ejecuta la función `nombre_completo` pasándole el `nombre` y `apellido` como dos argumnetos y retorna la frase que contiene el nombre completo._**

```python
nombre_completo = lambda nombre, apellido: f"Mi nombre completo es: {nombre} {apellido}"

nombre_completo("Caty", "Gonzáles")
```

## ¿Qué es un paquete pip?

Es la herramienta (gestos de paquetes) oficial para instalar paquetes de Python. Sirve para instalar, actualizar y eliminar librerías externas que podemos usar en nuestros proyectos.

Los paquetes son librerias externas de código python que extienden el código base de python y amplifican su funcionalidad. Permite aprovechar código ya hecho, ahorrando tiempo. Facilita compartir y usar librerías entre desarrolladores

```python
pip install requests # Instalar
pip install --upgrade requests # Actualizar
pip uninstall requests # Desinstalar
```
