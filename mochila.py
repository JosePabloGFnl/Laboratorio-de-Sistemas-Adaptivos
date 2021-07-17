import random
from random import randint
import math

#Generación de la población
poblacion = [303, 1003, 588, 39, 729, 750]
objetosrange = 10
objetos = pow(objetosrange, 2) - 1
aptitudtotal = 0
mejoraptitud = 0
diccaptitudes = {}
listaaptitudes = []
mejorindividuo = ""
iteraciones = 1
numerosbinarios = []

for i in poblacion:
    binario = bin(i)[2:]
    binario = binario.zfill(objetosrange)
    numerosbinarios.append(binario)

print("\n")
print(f"Población inicial:")
for i in range(len(numerosbinarios)):
    print(f"[{poblacion[i]}]  {numerosbinarios[i]}")

pesoobjetos = [47, 43, 44, 35, 33, 36, 24, 49, 41, 29]
gananciaobjetos = [67, 15, 33, 75, 81, 44, 17, 72, 91, 16]
capacidad = 220

#Evaluación
for i in range(iteraciones):
    aptitudtotal = 0
    for cromosoma in numerosbinarios:
        aptitud = 0.0
        peso = 0.0
        for i in range(0, objetosrange):
            aptitud += int(cromosoma[i]) * gananciaobjetos[i]
            peso += int(cromosoma[i]) * pesoobjetos[i]
        if peso > capacidad:
            aptitud = 0.0
        if aptitud > mejoraptitud:
            mejoraptitud = aptitud
            mejorindividuo = cromosoma
        listaaptitudes.append(aptitud)
        diccaptitudes[cromosoma] = aptitud
        aptitudtotal += aptitud
    print("\n")
    print(f"Evaluacion:")
    for i in range(len(listaaptitudes)):
        print(f"[{listaaptitudes[i]}]  {numerosbinarios[i]}")
    print("--------------")
    print(f"Aptitud Total = {aptitudtotal}")

#Selección
    lista_ruleta = []
    lista_ruleta2 = []
    for i in listaaptitudes:
        lista_ruleta.append(round((i / aptitudtotal) * 100))
    ruleta_unit = 0
    for cromosoma in diccaptitudes:
        ruleta_unit = int(round((diccaptitudes[cromosoma] / aptitudtotal) * 100))
        for i in range(0, ruleta_unit):
            lista_ruleta2.append(cromosoma)
    random.shuffle(lista_ruleta2)

    print("\n")
    print(f"Selección")
    for i in range(len(numerosbinarios)):
        print(f"Al cromosoma {numerosbinarios[i]} le corresponden {lista_ruleta[i]} espacios.")
    padre1 = []
    padre2 = []
    parejas = 3
    for i in range(parejas):
        padrey = random.choice(lista_ruleta2)
        while True:
            padrex = random.choice(lista_ruleta2)
            if (padrex != padrey):
                break
        padre1.append(padrex)
        padre2.append(padrey)
    print("\n")
    print(f"Parejas")
    for i in range(parejas):
        print(f"{padre1[i]}   \t {padre2[i]}")

#Cruce
    punto_cruce = 3
    hijos = []
    print("\n")
    print(f"Cruce")
    print(f"Punto cruce = 3")
    for i in range(parejas):
        hijo1 = padre2[i][:punto_cruce] + padre1[i][punto_cruce:]
        hijo2 = padre1[i][:punto_cruce] + padre2[i][punto_cruce:]
        hijos.append(hijo1)
        hijos.append(hijo2)
        print(f"Padre1: {padre1[i]} Padre2: {padre2[i]} \t Hijo 1: {hijo2} Hijo 2:{hijo1}")
    lista_ruleta.clear()
    lista_ruleta2.clear()

#Mutación
    probabilidad = 0.1
    print(f"Punto cruce === 0.1")
    numerosbinarios.clear()
    for cromosoma in hijos:
        cromosomamutado = ''
        for gen in cromosoma:
            resultado = random.randint(1, 10) / 10.0
            if (resultado <= probabilidad):
                cromosomamutado += str(abs(int(gen) - 1))
            else:
                cromosomamutado += gen
        numerosbinarios.append(cromosomamutado)
    print("\n")
    print(f"Mutacion")
    for i in range(len(numerosbinarios)):
        print(f"Mutando gen del cromosoma \t {numerosbinarios[i]}")
    hijos.clear()
    listaaptitudes.clear()


aptitudTotal = 0
for cromosoma in numerosbinarios:
    aptitud = 0.0
    peso = 0.0
    for i in range(0, objetosrange):
        aptitud += int(cromosoma[i]) * gananciaobjetos[i]
        peso += int(cromosoma[i]) * pesoobjetos[i]
    if peso > capacidad:
        aptitud = 0.0
    if aptitud > mejoraptitud:
        mejorindividuo = cromosoma
        mejoraptitud = aptitud
    listaaptitudes.append(aptitud)
    diccaptitudes[cromosoma] = aptitud
    aptitudtotal += aptitud
print("\n")
print(f"Resultados:")
print("***********************************")
print(f"Mejor individuo: {mejorindividuo}")
print(f"Mejor aptitud: {mejoraptitud}")
print("***********************************")

