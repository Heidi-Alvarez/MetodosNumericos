#!/home/heidi/Computadores/Metodos Numericos/Clase


import math

def fun(x):
    f=math.sin(x)
    return f

def integral(x):
    itg=-math.cos(x)
    return itg

xi=0.0; xf=math.pi/4.0;

n=1.0
h=(xf-xi)/n
integral1=h*(fun(xi)+fun(xi+h))/2.0

n=2.0
h=(xf-xi)/n
integral2=(h*(fun(xi)+4.0*fun(xi+h)+fun(xi+2.0*h)))/3.0

n=3.0
h=(xf-xi)/n
integral3=(3.0*h*(fun(xi)+3.0*fun(xi+h)+3.0*fun(xi+2.0*h)+fun(xi+3.0*h)))/8.0

n=4.0
h=(xf-xi)/n
integral4=(2.0*h*(7.0*fun(xi)+32.0*fun(xi+h)+12.0*fun(xi+2.0*h)+32.0*fun(xi+3.0*h)+7.0*fun(xi+4.0*h)))/45.0

print integral1,integral(xf)-integral(xi)
print integral2,integral(xf)-integral(xi)
print integral3,integral(xf)-integral(xi)
print integral4,integral(xf)-integral(xi)

n=0.0; h=(math.pi/4.0)/(n+2.0); xi=h; xf=math.pi/4.0 

