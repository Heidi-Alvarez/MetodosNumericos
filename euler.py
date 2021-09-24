#!/home/heidi/Computadores/Metodos Numericos/Tarea2

import math
import pylab as p

def factorial(n):
	factorial=1
	for i in range(1,n+1):
		factorial*=i
	return factorial

npuntos=101; delta=6.0/(npuntos-1.0); Ngrados=[6,10,20]; xx=[]; euler=[];

for i in range(npuntos):
	x=-3.0+delta*i
        eu=math.exp(x)
        xx.append(x)
	euler.append(eu)

for k in Ngrados:
	funcion=[]
	for i in range(npuntos):
		x=-3.0+delta*i
		pol=0.0
		for j in range(k):
			fac=factorial(j)
			pol+=x**j/fac
		funcion.append(pol)
 	p.plot(xx,funcion)
	p.plot(xx,euler)

p.show()

