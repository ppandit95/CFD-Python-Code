#solve 2D Convection, represented by the pair of coupled partial differential equations below:
#∂u∂t+u∂u∂x+v∂u∂y=0
#∂v∂t+u∂v∂x+v∂v∂y=0

#The initial conditions are 
#u, v ={2 for x,y∈(0.5,1)×(0.5,1), 1 everywhere else

#The boundary conditions are
#u=1, v=1 for {x=0,2 ; y=0,2

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot,cm
import numpy

nx=51
ny=51
nt=20
dx=2/(nx-1)
dy=2/(ny-1)
sigma=0.29
c=1
dt=sigma*dx

x=numpy.linspace(0,2,nx)
y=numpy.linspace(0,2,ny)

u=numpy.ones((ny,nx))
v=numpy.ones((ny,nx))
un=numpy.ones((ny,nx))
vn=numpy.ones((ny,nx))


u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
v[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

X, Y = numpy.meshgrid(x, y)
fig = pyplot.figure(figsize=(25, 17), dpi=300)
ax1 = fig.add_subplot(221,projection='3d')
ax1.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('IC for u')

ax2 = fig.add_subplot(222,projection='3d')
ax2.plot_surface(X, Y, v, cmap=cm.hsv, rstride=2, cstride=2)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title('IC for v')


for n in range(nt):
	un=u.copy()
	vn=v.copy()
	u[1:, 1:] = (un[1:, 1:] - (un[1:, 1:] * c * dt / dx * (un[1:, 1:] - un[1:, :-1])) - vn[1:, 1:] * c * dt / dy * (un[1:, 1:] - un[:-1, 1:]))
	v[1:, 1:] = (vn[1:, 1:] -(un[1:, 1:] * c * dt / dx * (vn[1:, 1:] - vn[1:, :-1])) - vn[1:, 1:] * c * dt / dy * (vn[1:, 1:] - vn[:-1, 1:]))

	u[0,:]=1
	u[-1,:]=1
	u[:,0]=1
	u[:,-1]=1

	v[0,:]=1
	v[-1,:]=1
	v[:,0]=1
	v[:,-1]=1



ax3 = fig.add_subplot(223,projection='3d')
ax3.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)
ax3.set_xlabel('$x$')
ax3.set_ylabel('$y$')
ax3.set_title('Computation for u')

ax4=fig.add_subplot(224,projection='3d')
ax4.plot_surface(X,Y,v,cmap=cm.hsv,rstride=2,cstride=2)
ax4.set_xlabel('$x$')
ax4.set_ylabel('$y$')
ax4.set_title('Computation for v')

pyplot.savefig('Output/2DNonlinearConvection.png')



