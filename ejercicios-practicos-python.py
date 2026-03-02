# Cree un bucle For de Python.

for num in range(20):
  print(num)

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(uno, dos, tres):
  return uno + dos + tres

print(suma(1,2,3))

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
suma_lambda = lambda uno, dos, tres: uno + dos + tres

print(suma_lambda(1,2,3))

# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Henry'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

coincide = False  

for huesped in lista_nombre:
    if huesped == nombre:
        coincide = True
        break  

if coincide:
    print(f"El nombre '{nombre}' coincide con un valor de la lista")
else:
    print(f"El nombre '{nombre}' NO coincide con ningún valor de la lista.")

  
