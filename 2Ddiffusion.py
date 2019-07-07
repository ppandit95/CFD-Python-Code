#the 2D-diffusion equation is :
#∂u/∂t=ν∂2u/∂x2+ν∂2u/∂y2
#Using forwared differencing for time stepping and central differencing for spatial stepping

import numpy
from matplotlib import pyplot,cm
from mpl_toolkits.mplot3d import Axes3D

nx=501
ny=501
nt=250
nu=0.08
dx=2/(nx-1)
dy=2/(ny-1)
sigma=0.23
dt=sigma*dx*dy/nu

x=numpy.linspace(0,2,nx)
y=numpy.linspace(0,2,ny)

u=numpy.ones((ny,nx))
un=numpy.ones((ny,nx))

u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2  

fig=pyplot.figure(figsize=(20, 20), dpi=300)
X, Y = numpy.meshgrid(x, y)


ax1=fig.add_subplot(211,projection='3d')
surf1=ax1.plot_surface(X,Y,u,rstride=2, cstride=2, cmap=cm.Paired,linewidth=0, antialiased=False)
ax1.set_xlim(0, 2)
ax1.set_ylim(0, 2)
ax1.set_zlim(1, 2.5)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_title('IC for diffusion equation')


def diffuse(nt):
	for n in range(nt+1):
		un=u.copy()
		u[1:-1, 1:-1] = (un[1:-1,1:-1] + nu * dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) + nu * dt / dy**2 * (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))

	

diffuse(nt)

ax2=fig.add_subplot(212,projection='3d')
surf2=ax2.plot_surface(X,Y,u,rstride=2, cstride=2, cmap=cm.Dark2,linewidth=5, antialiased=False)

ax2.set_xlim(0, 2)
ax2.set_ylim(0, 2)
ax2.set_zlim(1, 2.5)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_title('Computation of  diffusion equation')
fig.colorbar(surf2)
pyplot.savefig('Output/2Ddiffusion.png')





