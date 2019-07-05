import numpy
from matplotlib import pyplot
import pylab
pylab.ion()
for k in range (4):
	nx=41                                                           # No. of grid cells in the domain
	dx=2/(nx-1)                                                     #Grid Spacing inthe domain
	nt=25+9*k                                                           #No. of time steps
	dt=0.025                                                           #Time step size
	c=1                                                             #Wave-speed
	
	u=numpy.ones(nx)                                                  #Setting up the initial solution array for the problem
	u[int(.5/dx):int(1./dx+1)]=2                                    #Setting specific boundary condition
	pyplot.plot(numpy.linspace(0,2,nx),u, label='Input-'+str(k) )
	pylab.legend(loc='upper left')
#######################################################################################################################################
######################################################################################################################################
	un=numpy.ones(nx)                                                 #Setting up temporary array 
	for n in range(nt):
 	 un=u.copy()
 	 for i in range(1,nx):
  	  u[i]=un[i]-c*dt/dx*(un[i]-un[i-1])                              #Implementing Finite Difference Method
	
	pyplot.plot(numpy.linspace(0,2,nx),u,label='Output-'+str(k) )
	pylab.legend(loc='upper left')
	pyplot.savefig('1DConvection.png')
