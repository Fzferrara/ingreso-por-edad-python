# Pseudocodigo:
# # Paso 1. Solicitar al usuario que ingrese la edad del clinte.
# Mostrar mensaje: "Por favor ingrese la edad del cliente: "
# Leer el dato y asignarlo a la variable edad

edad = int(input("Por favor ingrese la edad del cliente: "))

# # Paso 2. Verificar si la edad ingresada cumple el requisito de ingreso.
# Si edad >= 18 entonces
#     asignales a la variable permitido verdadero
# Si no
#     asignales a la variable permitido Falso
# Fin Si
permitido = True
if edad >= 18:
    permitido = True
else:
    permitido = False
 
# permitido = True if edad >= 18 else False # ternario
  
# # Paso 3. Mostrar al usuario si su cliente puede ingresar a la disco.

# Si permitido es verdadero   
#     Mostrar mensaje: "Puedes ingresar a la discoteca"
# Sino
#     Mostrar mensaje: "Lo sentimos, no cumples con la edad minima de ingreso"
if permitido:
    print("Puedes ingresar a la discoteca")
else:
    print("Lo sentimos, no cumples con la edad minima de ingreso") 

# Fin si

# Fin