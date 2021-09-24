#! /home/heidi/Computadores/Metodos Numericos
from visual.graph import *
import random # genera numeros aleatorios
imax=13000 # numero de puntos

grafico=display(width=500,height=500,range=2)

x=0.5
y=0.0
z=-0.2


for i in range (1,imax): #para generar 13000
    r=random.random()

    if (r<0.1):
        x=0
        y=0.18*y
        z=0
        color1=color.orange
        

    elif (r>0.1 and r<0.7):
        x=0.85*x
        y=0.85*y+0.1*z+1.6
        z=-0.1*y+0.85*z

        color1=color.blue
    elif (r>0.7 and r<0.85):
        x=0.2*x-0.2*y
        y=0.2*x+0.2*y+0.8
        z=0.3*z
        color1=color.green

    else:
        x=-0.2*x+0.2*y
        y=0.2*x+0.2*y+0.8
        z=0.3*z
        color1=color.red


    xc=2.0*x
    yc=2.0*y-2.0
    zc=2.0*z-2.0
    points(pos=(xc,yc,zc),color=color1,size=0.02)

#ImportError: No module named visual.grapg
