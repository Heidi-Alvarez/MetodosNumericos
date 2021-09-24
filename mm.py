#!/home/heidi/Computadores/Metodos Numericos

Nx=int(raw_input('Ingrese el numero de puntos en x'))
Ny=int(raw_input('Ingrese el numero de puntos en y'))
xmin=float(raw_input('Ingrese el minimo valor de x'))
xmax=float(raw_input('Ingrese el maximo valor de x'))
ymin=float(raw_input('Ingrese el minimo valor de y'))
ymax=float(raw_input('Ingrese el maximo valor de y'))
dx=(xmax-xmin)/(Nx-1)
dy=(ymax-ymin)/(Ny-1)

def funcion(x,y):
	fun=x*x+y*y*y
	return fun
x=0
y=0
Cmin=1000
Cmax=-1000

for i in [xmin, xmax, dx]:
	x=x+dx
	for j in [ymin,ymax,dy]:
		y=y+dy
		z=funcion(x,y)
		if (z<Cmin):
			Cmin=z
			Xmin=x
			Ymin=y	
		if (z>Cmax):
			Cmax=z
			Xmax=x
			Ymax=y
print Cmin, Xmin, Ymin
print Cmax, Xmax, Ymax

