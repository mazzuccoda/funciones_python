# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    if numero_1 > numero_2:
        print(f"{numero_1} es mayor que {numero_2}")
    elif numero_2 > numero_1:
        print(f"{numero_2} es mayor que {numero_1}")
    else:
        print("Los 2 numeros son iguales")
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor en pantalla


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Complete la función "imprimir_mayor"
    imprimir_mayor(2, 10)

    print("terminamos")