#!/home/heidi/Computadores/Metodos Numericos/Tarea2

import math
import pylab as p

def factorial(n):
	fac=1
	for i in range(1,n+1):
		fac*=i
	return fac

npuntos=101; delta=6.0*math.pi/(npuntos-1.0); Ngrados=[20,30,40]; xx=[]; seno=[]

for i in range(npuntos):
	x=-3.0*math.pi+delta*i
	sen=math.sin(x)
	xx.append(x)
	seno.append(sen)

for k in Ngrados:
	funcion=[]
	for i in range(npuntos):
		x=-3.0*math.pi+delta*i
		fun=0.0
		for j in range(k):
			n=2*j+1
			fac=factorial(n)
			fun+=(-1)**j*x**n/fac
		funcion.append(fun)
	p.plot(xx,funcion)
	p.plot(xx,seno)

p.show()
