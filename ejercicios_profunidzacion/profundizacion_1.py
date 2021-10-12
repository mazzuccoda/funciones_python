# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problemla
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira la dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números.
Esa lista de datos se llamará "dados_tirados"
Lista "dados_tirados" se utiliza para guardar 5 dados, cada dado es de 6 caras,
es decir que cada dado puede valer un número de 1 a 6.

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió en esa tirada. 
Consultar los ejemplos vistos en clase en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una variable aparte llamda "contador_generala"
cuantas veces se repitió hasta ahora el número más repetido. 
Ese número será el candidato para busscar sacar generala.
Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4",
por lo canto el "contador_generala" valdrá 3, porque el primer número
más repetido fue 4, y este número salio tres veces en la primera tirada.

4) Debe volver a tira los dados, generar nuevos
números aleatorios.
Si en el contador "contador_generala" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados (5-3). 
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a contar cuantas veces aparece el número "4",
ya que es el número que estoy buscando almacenar para llegar a generala.
Se deberá aumentar el contador por cada cuatro que haya salido en la tirada.
Sino salió el "4" vuelvo a tirar sin aumentar el contador (repetir el punto 4)

5) Debe repetir este proceso hasta que el contador "contador_generala"
haya llegado a 5, es decir, he sacado 5 números iguales

NOTA: Recordar que en este ejemplo se buscó alcanzar la generala con "4" porque
fue el primero número más repetido en la primera tirada. Tener eso en cuenta que el
número que deberá buscar para alcanzar la generala depende de cual fue el más repetido
en la primera tirada.
'''

import random

# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice

#función para contar la cantidad de repetición de numero en un lista
def contar(lista,numero):
    return lista.count(numero)

#genera una lista aleatoria del 1 al 6
def lista_aleatoria(n):
    resultado = []
    for x in range(n):
        numero = random.randrange(1, 7)
        resultado.append(numero)
    return resultado

# cuanta la frecuencia de los numeros del 1-6 en unas lista
def contador_generala(lista):
    frecuencia = []
    for x in range(6):
        frecuencia.append(lista.count(x+1))
    return frecuencia

#selecciona el numero con mayor frecuencia y selecciona que numero es
def elegido (lista):
    maximo = 0
    numero_elegido = 0
    maximo = max(lista)
    numero_elegido = lista.index(maximo)+1
    return maximo,numero_elegido



# --------------------------------

if __name__ == '__main__':
    print("¡El juego de la generala!")

print("#############################################")
print("Comienza el Juego!!!, tiene 5 intentos")
print("#############################################")

n_dados = 5
numero_elegido = 0
frecuencia = 1

for x in range(5):
    print(f"tiro N° {x+1} con {n_dados} dados")
    tiro = lista_aleatoria(n_dados)
    print("dados tirados...")
    print(tiro)

    if n_dados == 5:
        seleccionar = elegido(contador_generala(tiro))
        print(f"El numero elegido es el {seleccionar[1]}, que salio {seleccionar[0]} veces")
        numero_elegido = seleccionar[1]
        frecuencia = seleccionar [0]
            
        if frecuencia > 1:
            n_dados -= frecuencia

    elif n_dados < 5 and n_dados > 0:
        frecuencia_elegido = contar(tiro,numero_elegido)
        if frecuencia_elegido > 0:
            n_dados -=frecuencia_elegido 
            #print(contar(tiro,numero_elegido))
            if n_dados == 0:
                print("GANO")
                break
    else:
        print("GANO")
        break

if n_dados > 0:
    print("PERDIO! JUEGE OTRA VEZ")
          
    # A partir de aquí escriba el código que
    # invoca a las funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

