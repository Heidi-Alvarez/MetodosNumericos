#!/home/heidi/Computadores/Metodos Numericos/Tarea5

import math

m=1.0
t=[0.0,1.0,2.0,3.0,4.0]
y=[100.0,95.1,80.4,55.9,21.6]
n=int(len(y))
xmin=t[0]
xmax=t[n-1]
delta=(xmax-xmin)/(n-1)
velocidad=[]
aceleracion=[]
Fuerza=[]
for i in range(n):
    if (i==0):
	v=(-3.0*y[i]+4.0*y[i+1]-y[i+2])/(2.0*delta)
	velocidad.append(v)
    elif (i==(n-1)):
	v=(-3.0*y[i]+4.0*y[i-1]-y[i-2])/(-2.0*delta)
	velocidad.append(v)
    else:
	v=(y[i+1]-y[i-1])/(2.0*delta)
	velocidad.append(v)

for i in range(n):
    if (i==0):
        a=(-3.0*velocidad[i]+4.0*velocidad[i+1]-velocidad[i+2])/(2.0*delta)
        aceleracion.append(a)
    elif (i==(n-1)):
        a=(-3.0*velocidad[i]+4.0*velocidad[i-1]-velocidad[i-2])/(-2.0*delta)
        aceleracion.append(a)
    else:
        a=(velocidad[i+1]-velocidad[i-1])/(2.0*delta)
        aceleracion.append(a)
    F=m*aceleracion[i]
    Fuerza.append(F)

print Fuerza 


