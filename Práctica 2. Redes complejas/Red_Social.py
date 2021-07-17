import sys
import pandas as pd
import numpy as np
df=pd.read_csv('Magos.csv')
L=np.asarray(df)

m=0
grados=[]

try:
	archivo=open('Magos.txt')
	lineas=archivo.readlines()
	archivo.close()
except IOError:
	print('No se pudo abrir el archivo')
	sys.exit(1)
	
n=len(lineas)

for linea in lineas:
	linea=linea.strip()
	celdas=linea.split()
	grado=0
	for celda in celdas:
		m=m + int(celda)
		grado=grado + int(celda)
	grados.append(grado)
		
m=m/2

densidad=2*m/(n*(n-1))

print('n: ',n)
print('m: ',m)
print('Densidad:',round(densidad,3))

for i in range(len(grados)):
	centralidad=grados[i]/(n-1)
	centralidad=round(centralidad,3)
	print("Grado v"+str(i)+"="+str(grados[i])+ " Centralidad: "+str(centralidad))
print('\n')
print('\n')
for i in range(7):
    if i ==0:
        n='Diego'
    if i ==1:
        n='Mario'
    if i ==2:
        n='Pablo'
    if i ==3:
        n='Christo'
    if i ==4:
        n='Alejandro'
    if i ==5:
        n='Gabriel'
    if i ==6:
        n='Christopher Nolan'
    for j in range(7):
        if j ==0:
            s='Diego'
        if j ==1:
            s='Mario'
        if j ==2:
            s='Pablo'
        if j ==3:
            s='Christo'
        if j ==4:
            s='Alejandro'
        if j ==5:
            s='Gabriel'
        if j ==6:
            s='Christopher Nolan'
        if L[i][j]==1:
            print(str(n)+' sigue a '+str(s))
        