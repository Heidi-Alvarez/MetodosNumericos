#!/home/heidi/Computadores/Metodos Numericos/Tarea1

import math 

Nx=101; Ny=101; deltax=2*math.pi/Nx; deltay=math.pi/Ny; Zmax=-2.0; Zmin=2.0

for i in range(Nx):
	x=-math.pi+deltax*i
	for j in range(Ny):
		y=-math.pi/2.0 +deltay*j
		f=math.sin(x)*math.cos(y)-math.cos(y/2.0 +math.pi/3.0)
		if(f<Zmin):
			Zmin=f
			Xmin=x
			Ymin=y
		if(f>Zmax):
			Zmax=f
			Xmax=x
			Ymax=y

print Zmin, Xmin, Ymin, Zmax, Xmax, Ymax
