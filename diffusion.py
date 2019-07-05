#The one-dimensional diffusion equation is:
#∂u∂t=nu∂2u∂x2

import numpy
from matplotlib import pyplot
import pylab
for p in range(41):
	nx=41*(p+1)
	dx=2/(nx - 1)
	nt=20
	nu=0.3
	sigma=0.2
	dt=sigma*dx**2/nu
	u=numpy.ones(nx)
	u[int(0.5/dx):int(1/dx+1)]=2
	pyplot.plot(numpy.linspace(0,2,nx),u)
	un=numpy.ones(nx)
	for n in range(nt):
		un=u.copy()
		for i in range(1,nx-1):
			u[i]=un[i]+nu*dt/dx**2*(un[1+i]-2*un[i]+un[i-1])
	if nx==1681 :
		pyplot.plot(numpy.linspace(0,2,nx),u,label='Final ref.-'+str(nx))
		pylab.legend(loc='upper right')
	else :
		pyplot.plot(numpy.linspace(0,2,nx),u)	

	
pylab.title('Variation in accuracy with grid refinement')
pyplot.savefig('Diffusion-grid-refinement.png')
pyplot.close()

for j in range(1,4):
	nx=41
	dx=2/(nx - 1)
	nt=20
	nu=0.3
	sigma=0.2+j/10.0
	dt=sigma*dx**2/nu
	u=numpy.ones(nx)
	u[int(0.5/dx):int(1/dx+1)]=2
	pyplot.plot(numpy.linspace(0,2,nx),u)
	un=numpy.ones(nx)
	for n in range(nt):
		un=u.copy()
		for i in range(1,nx-1):
			u[i]=un[i]+nu*dt/dx**2*(un[1+i]-2*un[i]+un[i-1])
	pyplot.plot(numpy.linspace(0,2,nx),u)
	
pylab.title('Variation in accuracy with CFL number')
pyplot.savefig('Diffusion-CFL.png')	
	

