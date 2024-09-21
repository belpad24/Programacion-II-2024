print("Hola Bito Gracias por ayudarme")
#Un diccionario en Python es una colección de pares clave-valor. Es una estructura de datos 
# que permite almacenar información de manera que cada elemento se puede acceder a través de una 
# clave única. Los diccionarios son mutables, lo que significa que puedes cambiar su contenido 
# después de haberlos creado.

#Aquí tienes un ejemplo de un diccionario en Python:
# Definimos un diccionario con información de una persona
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"}

# Accedemos a los valores utilizando las claves
print("Nombre:", persona["nombre"])  # Salida: Nombre: Juan
print("Edad:", persona["edad"])      # Salida: Edad: 30
print("Ciudad:", persona["ciudad"])  # Salida: Ciudad: Madrid

# Agregamos un nuevo par clave-valor
persona["profesión"] = "Ingeniero"

# Imprimimos el diccionario actualizado
print(persona)
#En este ejemplo, el diccionario  `persona`  contiene 
# información sobre una persona, y puedes acceder a los
# datos utilizando las claves como "nombre", "edad" y
# "ciudad". También puedes agregar nuevos pares clave-valor, como "profesión".