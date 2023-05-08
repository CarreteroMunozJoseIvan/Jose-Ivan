import numpy as np
import random

tamaño = 10

def crear_tablero(tamaño):
    return np.full((tamaño,tamaño), " ")

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        tablero[casilla] = "X"
        print("Tocado")
        while tablero[casilla] == "O":
            disparar(casilla, tablero)
        
    elif tablero[casilla] == "X":
        print("Ya dijiste esa") 
    elif tablero[casilla] == "-": #Esto no se porque no va
        print("Ya dijiste esa")

    else:
        tablero[casilla] = "-"
        print("Agua")
    return tablero

def crear_barco_random(eslora, tamaño):
    barco_random = []
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    barco_random.append((fila_random,columna_random))
    orient = random.choice(["N","S","E","O"])

    while len(barco_random) < eslora:
        if orient == "O":
            columna_random = columna_random - 1 
        elif orient == "E":
            columna_random = columna_random + 1
        elif orient == "N":
            fila_random = fila_random - 1
        elif orient == "S":
            fila_random = fila_random + 1

        if fila_random not in range(tamaño) or columna_random not in range(tamaño):
            fila_random = random.randint(0,9)
            columna_random = random.randint(0,9)
            barco_random = []
            barco_random.append((fila_random,columna_random))
        else:
            barco_random.append((fila_random,columna_random))

        # print(barco_random)
    return barco_random

def turno_cpu(tablero):
    
         
    fila = random.randint(0, len(tablero) - 1)
    columna = random.randint(0, len(tablero[0]) - 1)
    casilla = (fila, columna)
    disparar(casilla, tablero)
    if tablero[fila][columna] == " ":
        
        print("Agua")

    elif tablero[fila][columna] == "O":

        tablero[fila][columna] == "X"

    for fila in tablero:
        print(" ".join(fila))
        break
    
                     
             
    return tablero

        
