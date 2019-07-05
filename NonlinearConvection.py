import numpy
from matplotlib import pyplot



nx=15
dx=2/(nx-1)
nt=25
dt=0.025

u=numpy.ones(nx)
u[int(0.5/dx):int(1/dx+1)]=2

un=numpy.ones(nx)
for i in range(nt):
 un=u.copy()
 for j in range(1,nx):
  u[j]=un[j]-un[j]*dt/dx*(un[j]-un[j-1])


pyplot.plot(numpy.linspace(0,2,nx),u)
pyplot.savefig('NonlinearConvection.jpg')


