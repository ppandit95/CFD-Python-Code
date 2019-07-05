#The PDE governing 2-D Linear Convection is written as
#∂u∂t+c∂u∂x+c∂u∂y=0
#The timestep is discretized as a forward difference and both spatial steps will be discretized as backward differences.
#We solve this equation with the following initial conditions:
#u(x,y)={2  for0.5≤x,y≤1 and  1 everywhere else

#and boundary conditions:
#u=1 for {x=0,2as well as y=0, 2
from mpl_toolkits.mplot3d import Axes3D

import numpy
from matplotlib import pyplot,cm

nx=81
ny=81
nt=100
c=1
dx=2.0/(nx-1)
dy=2./(ny-1)
sigma=0.2
dt=sigma*dx

x=numpy.linspace(0,2,nx)
y=numpy.linspace(0,2,nx)

u=numpy.ones((ny,nx))
un=numpy.ones((ny,nx))

u[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)]=2      #Assigning intial conditions
fig=pyplot.figure(figsize=(11,7),dpi=100)
ax=fig.gca(projection='3d')
X,Y=numpy.meshgrid(x,y)
surf = ax.plot_surface(X, Y, u[:], cmap=cm.spring)
pyplot.savefig('Output/2DLinearConvectionIC.png')

for n in range(nt) :
	un=u.copy()
	row,col=u.shape
	for j in range(1,row):
		for i in range(1,col):
			u[j,i]=(un[j,i]-(c*dt/dx*(un[j,i]-un[j,i-1]))-(c*dt/dy*(un[j,i]-un[j-1,i])))
			u[0,:]=1
			u[-1,:]=1
			u[:,0]=1
			u[:,-1]=1

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.flag)

pyplot.savefig('Output/2DLinearConvection.png')

pyplot.close()
