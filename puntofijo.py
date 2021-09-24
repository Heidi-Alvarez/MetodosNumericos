#!/home/heidi/Computadores/Metodos Numericos/Segunda

import numpy as np
import math

def fun(x):
	m=1.0
    	h=100.0
	g=9.8
	k=0.1
	a=k/(m*g)
	b=(g*m**2)/(k**2)
	f=a*(h+b*(1-math.exp(-k*x/m)))
	return f

error=1e-7; errort=10
t=0.0; T=1.0
while(np.abs(errort)>error):
	T=fun(t)
	errort=T-t
	t=T

print 'El tiempo en segundos que se demora en caer el objeto es %f'%T
