#Burgers' equation in one spatial dimension looks like this:
#∂u∂t+u∂u∂x=ν∂2u∂x2
#Using forward difference for time, backward difference for space and central difference for second derivative 
#Our initial condition for this problem is going to be:
#u= -2v/phi∂phi/∂x+4
#phi=exp(-x**2/4v)+exp(-(x-2pi)**2/4v)
#We are implementing periodic boundary condition as 
#u(0)=u(2pi)

import numpy
import sympy
from sympy import init_printing
init_printing(use_latex=True)
x,nu,t = sympy.symbols('x nu t')
phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
       sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))
phiprime = phi.diff(x)
from sympy.utilities.lambdify  import lambdify
u= -2*nu*(phiprime/phi)+4 

ufunc = lambdify((t, x, nu), u)

from matplotlib import pyplot

nx=191
nt=50
dx=2*numpy.pi/(nx-1)
nu=0.07
dt=dx*nu

x=numpy.linspace(0,2*numpy.pi,nx)
un=numpy.empty(nx)
t=0

u=numpy.asarray([ufunc(t,x0,nu) for x0 in x])

for n in range(nt):
	un=u.copy()
	for i in range(1,nx-1):
		u[i]=un[i]-un[i]*dt/dx*(un[i]-un[i-1])+nu*dt/dx**2 *(un[i+1]-2*un[i]+un[i-1])
		u[0]=un[0]-un[0]-un[0]*dt/dx*(un[0]-un[-2])+nu*dt/dx**2 *(un[1]-2*un[0]+un[-2])
		u[-1]=u[0]

u_analytical=numpy.asarray([ufunc(nt*dt,xi,nu) for xi in x])
pyplot.figure(figsize=(11, 7), dpi=300)
pyplot.plot(x,u, marker='o', lw=2, label='Computational')
pyplot.plot(x, u_analytical, label='Analytical')
pyplot.xlim([0, 2 * numpy.pi])
pyplot.ylim([0, 10])
pyplot.legend()
pyplot.savefig('Output/burgerseq.png')

