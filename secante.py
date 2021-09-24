#!/home/heidi/Computadores/Metodos Numericos/Segunda

import numpy as np
import math

def fun(x):
	m=1.0
    	h=100.0
	g=9.8
    	k=0.1
	f=h-(m*g*x)/k +(m**2*g*(1.0-math.exp(-k*x/m)))/k**2
	return f

error=1e-7
t=0.0; T=6.0
errort=(t-T)/T

while(np.abs(errort)>error):
	x=T-fun(T)*(T-t)/(fun(T)-fun(t))
	errort=x-T
	t=T
	T=x

print 'El tiempo en segundos que se demora en caer el objeto es %f'%x
