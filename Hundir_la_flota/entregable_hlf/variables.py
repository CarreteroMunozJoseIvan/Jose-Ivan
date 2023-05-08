
import sys
print (sys.path)
from classes import *
from functions import *

numero_slora = {"barco1": Barco(1), "barco2": Barco(1), "barco3": Barco(1), "barco4": Barco(1), "barco5": Barco(2), "barco6": Barco(2), "barco7": Barco(2), "barco8": Barco(3), "barco9": Barco(3), "barco10": Barco(4)}
lista_barcos = []
lista_barcos_CPU = []
vidas = vidas_CPU = 0


for i in numero_slora:
    vidas += numero_slora[i].eslora
for i in numero_slora:
    vidas_CPU += numero_slora[i].eslora

for i in numero_slora:
    barco = crear_barco_random(numero_slora[i].eslora, tamaño)
    lista_barcos.append(barco)
for i in numero_slora:
    barco = crear_barco_random(numero_slora[i].eslora, tamaño)
    lista_barcos_CPU.append(barco)
print(lista_barcos)
print(vidas)