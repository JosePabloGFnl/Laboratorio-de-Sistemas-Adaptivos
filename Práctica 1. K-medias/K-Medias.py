'''

Algunas funciones importantes:

 len(lista)
Devuelve la cantidad de elementos que tiene lista (si es lista anidada, serian los elementos del primer nivel).

 range(desde donde, hasta donde, cuanto avanzar)
Se utiliza junto con ciclos para determinar de que valor a que valor ira la variable del ciclo. Si solo usamos range(hasta donde), se asume que se empieza desde cero y se avanza uno.

 sys.float_info.max [Usar libreria sys]
Regresa el numero mas grande de punto flotante que tiene registrado Python

 pow(numero, potencia) [Usar libreria math]
Eleva numero a la potencia indicada.

'''

from math import *
import sys

'''
  Entradas: puntoA y puntoB -- son listas numericas de cualquier longitud (debe ser la misma longitud en ambas listas).
  Salida: Distancia euclidiana entre las listas.''' 
def calcularDistanciaEuclidiana(puntoA, puntoB):
    suma=0
    for i in range(len(puntoA)):
        suma=suma+pow(puntoA[i]-puntoB[i],2)
    return sqrt(suma)

#Datos. Contexto: colores
vectores=[[100,85,10],[70,50,90],[80,80,80],[50,85,70],[90,60,40],[60,70,95],[65,70,90]]
centroides=[[100,0,0],[0,100,0],[0,0,100]]

grupos=[["1.Vida"],["2.Fuerza"],["3.Velocidad"]]

#Asignacion de grupos
for i in range(len(vectores)):
    distanciaMasCercana=sys.float_info.max
    centroideMasCercano=-1
    for j in range(len(centroides)):
        distancia=calcularDistanciaEuclidiana(vectores[i],centroides[j])
        if distancia<distanciaMasCercana:
            distanciaMasCercana=distancia
            centroideMasCercano=j+1
    grupos.append(centroideMasCercano)

print(grupos)

#print(centroides)