#!/home/heidi/Computadores/Metodos Numericos/Tarea5

import math
import pylab as p

m=1.0 #kg
t=[0.0,1.0,2.0,3.0,4.0] #segundos
y=[100.0,95.1,80.4,55.9,21.6] # metros
V=[] # metros/segundo
F=[] #Newtons

n=int(len(t))

for i in range(1,n-1):
	v=(y[i+1]-y[i-1])/(2*i)
	V.append(v)

n=int(len(V))

for i in range(1,n-1):
	a=(V[i+1]-V[i-1])/(2*i)
	f=m*a
	F.append(f)

print F
