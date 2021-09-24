#! /home/heidi/Computadores/Metodos Numericos/Clase

import pylab as p

i=100; n=10; delta=2.0/i; Leg=[[0.0]*i]*n; Leg[1]=[1.0]*i; xx=[0.0]*i

for j in range(2,n):
	a=(2*(j-1)+1)/(j+1)
	b=1/j
	for l in range(1,100):
		x=delta*l
		c=Leg[j-2][l]
		d=Leg[j-1][l]
		P=a*x*c-b*d
		Leg[j][l]=P
		xx[l]=l


#for l in range(0,n-1):	
#	p.plot(Leg)

p.plot(Leg)
p.show()
