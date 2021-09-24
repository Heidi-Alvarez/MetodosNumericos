#!/home/heidi/Computadores/Metodos Numericos/Tarea2

import math
import numpy as np
import pylab as p

npuntos=101; delta=1.8/(npuntos-1); Ngrados=[6,12,20,50]; xx=[]; fun=[]; com=0.0

def valor(x):
	val=3.0/(1.0-x)
	return val

for i in range(npuntos):
	x=-0.9+delta*i
	funcion=3.0/(1.0-x)
	xx.append(x)
	fun.append(funcion)

for k in Ngrados:
	polinomios=[]
	for i in range(npuntos):
		x=-0.9+delta*i
		pol=0.0
		for j in range(k):
			pol+=3*x**j
		polinomio=pol
		VAL=valor(x)
		des=np.abs(pol-VAL)
		if(des>com):
			com=des
			X=x
		polinomios.append(polinomio)
	p.plot(xx,polinomios)
	p.plot(xx,fun)


print 'La desviacion maxima es des=%.3f en el valor de x=%.1f'%(com,X)

p.show()
