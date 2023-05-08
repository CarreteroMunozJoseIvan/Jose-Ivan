from functions import *
import sys
print (sys.path)
from classes import *
from variables import *


print("Bienvenido al hundir la flota!")
option = input("Quieres jugar primero una demo?")

if option.lower() == "si":

    tablero = crear_tablero(tamaño)
    tablero_CPU = crear_tablero(tamaño)

    
else:

    tablero = crear_tablero(tamaño)
    tablero_CPU = crear_tablero(tamaño)

    for barco in lista_barcos:
        tablero = colocar_barco(barco, tablero)
    for barco in lista_barcos_CPU:
        tablero_CPU = colocar_barco(barco,tablero_CPU)


    vidas
    vidas_CPU

    while (vidas > 0) or (vidas_CPU > 0):

        while "O" in tablero or "O" in tablero_CPU:
            
            fila_disparo = int(input("Qué fila disparas (0-9)?"))
            columna_disparo = int(input("Qué columna disparas (0-9)?"))
            mi_turno = disparar((fila_disparo, columna_disparo), tablero_CPU)
            vidas -= 1
            print(tablero, vidas)
            turno_cpu(tablero)
            vidas_CPU -= 1
            print(vidas_CPU)
            
           
##### LO Que me ha faltado por averiguar es como mostrar el tablero de la CPU sin los barcos 

        
        

        

        


