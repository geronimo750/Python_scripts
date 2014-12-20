#!/usr/bin/env python
# _*_ coding utf-8 _*_
#
# this work is licensed under a Creative Commons 
# Attribution-NonCommercial-ShareAlike 3.0 Unported License
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# Based on:
# http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/
#
# Use at your own risk!
#
from timeit import Timer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from Tkinter import *
import ttk

def tdma(a, b, c, d):
	""" tridiagonal matrix solver
	see wikipedia (tdma) entry for more details"""
  
	n = len(a) # n is the numbers of rows, a and c has length n-1
	cp = c;
	dp = d;
	xx = np.zeros(n)

	# Gaussian Elimination
	cp[0] = c[0]/b[0]
	dp[0] = d[0]/b[0]

	for i in xrange(1,n):
		cp[i] = c[i]/(b[i] - cp[i-1]*a[i])
		dp[i] = (d[i] - dp[i-1]*a[i])/(b[i]-cp[i-1]*a[i])

	# backward substitution
	xx[n-1] = dp[n-1]
	for i in reversed(xrange(n-1)):
		xx[i] = dp[i]-cp[i]*xx[i+1]

	return xx # return the solution

def initialize_flat_plate(nx,ny,uinf):
	""" set initial values for all variables"""
	v = np.zeros((ny,nx));
	u = np.zeros((ny,nx));

	## ##  Boundary Conditions
	u[:,0] = uinf; 	##  Inlet
	v[:,0] = 0.; 	##  Inlet
	u[0,:] = 0.; 	##  Wall
	v[0,:] = 0.; 	##  Wall
	u[ny-1,:] = uinf; ##  Top, free stream

	return u,v
     
def solve_flow(nx,ny,dx,dy,u,v,nu):
	""" solve flow problem by marching along the x-direction """

	##  March in the x direction
	A = np.zeros(ny);
	B = np.zeros(ny);
	C = np.zeros(ny);
	D = np.zeros(ny);
	for i in xrange(nx-1):

		##  Determine parameters A,B,C,D in TDMA method
		# near surface points
		j = 1
		A[j] = 0.;
		B[j] = 2*nu/(dy*dy) + u[j,i]/dx;
		C[j] = - nu/(dy*dy) + v[j,i]/2/dy;
		D[j] = u[j,i]*u[j,i]/dx - (- nu/(dy*dy) - v[j,i]/2/dy)*u[j-1,i+1];

		# inner points
		A[2:ny-2] = - nu/(dy*dy) - v[2:ny-2,i]/2/dy;
		B[2:ny-2] = 2*nu/(dy*dy) + u[2:ny-2,i]/dx;
		C[2:ny-2] = - nu/(dy*dy) + v[2:ny-2,i]/2/dy;
		D[2:ny-2] = u[2:ny-2,i]*u[2:ny-2,i]/dx ;
		
		# outer points
		j = ny-2
		A[j] = - nu/(dy*dy) - v[j,i]/2/dy;
		B[j] = 2*nu/(dy*dy) + u[j,i]/dx;
		C[j] = 0;
		D[j] = u[j,i]*u[j,i]/dx - (- nu/(dy*dy) + v[j,i]/2/dy)*u[j+1,i+1];

		##  solve for u using linear system of equation scipy routine
		usol = tdma(A[1:-1],B[1:-1],C[1:-1],D[1:-1]);
		u[1:ny-1,i+1] = usol;

		# solve for v(j,i+1) based on known u
		for j in xrange(1,ny):
			v[j,i+1] = v[j-1,i+1] - dy/2/dx*(u[j,i+1] - u[j,i] + u[j-1,i+1] - u[j-1,i])

def post_process(X,Y,u,v,uinf):
	""" output flowfield quantities """
	
	fig = plt.figure(figsize = (11,7), dpi=100)
	plt.subplots_adjust(left=0.075, bottom=0.06, right=0.95, top=0.94, wspace=0.15)

	xStart = min(X[0,:])
	yStart = min(Y[:,0])
	xEnd = max(X[0,:])
	yEnd = max(Y[:,0])
	
	# velocity vectors
	bs = int(len(u)/20)
	if bs < 1: bs = 1
	print(bs)
	plt.subplot(3,1,2)
	levels = [.99,]
	CS3 = plt.contour(X, Y, np.sqrt(u*u+v*v+1e-5)/uinf, levels,extend='both', cmap='copper')
	plt.clabel(CS3, inline=1, fontsize=14)
	plt.quiver(X[::bs, ::bs], Y[::bs, ::bs], u[::bs, ::bs], v[::bs, ::bs])
	plt.title('Velocity Vectors and boundary layer thickness, $u = 0.99U_0$')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.xlim(xStart,xEnd)
	plt.ylim(yStart,yEnd)

	plt.subplot(3,1,1)
	#plt.pcolor(X, Y, np.sqrt(u*u+v*v+1e-5)/uinf, cmap='coolwarm')
	plt.pcolor(X, Y, np.sqrt(u*u+v*v+1e-5)/uinf, cmap='gist_ncar')
	plt.colorbar(ticks=[0.0, 0.25, 0.5, 0.75, 1], orientation='horizontal')
	plt.title('Velocity Contours, $u/U_0$')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.xlim(xStart,xEnd)
	plt.ylim(yStart,yEnd)
	
	plt.subplot(3,1,3)
	plt.streamplot(X,Y,u,v,density=0.50,linewidth=1,arrowsize=1,arrowstyle='->')
	plt.title('Streamlines')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.xlim(xStart,xEnd)
	plt.ylim(yStart,yEnd)
	
	plt.show()

def calc_reynolds_number(u,rho,x,mu):
	return u*rho*x/mu

def calc_delta(Rey,x):
	return 5.*x/np.sqrt(Rey)
 
def calculate(*args):
	""" set up and launch solver in interactive mode """
	try:
		value = float(rho.get())
		rho_val = value
		value = float(mu.get())
		mu_val = value
		value = float(uinf.get())
		uinf_val = value
		value = float(L.get())
		L_val = value
		value = float(H.get())
		H_val = value
		value = float(nx.get())
		nx_val = int(value)
		value = float(ny.get())
		ny_val = int(value)
		
		Re_L 	= calc_reynolds_number(uinf_val,rho_val,L_val,mu_val);
		delta_L = calc_delta(Re_L,L_val);	## laminar flow
		rey.set(Re_L)
		delta.set(delta_L)
		
		dx 	= L_val/(nx_val-1);
		dy 	= H_val/(ny_val-1);
		x 	= np.linspace(0,L_val,nx_val)
		y 	= np.linspace(0,H_val,ny_val)
		X,Y 	= np.meshgrid(x,y)

		#initial conditions
		u,v = initialize_flat_plate(nx_val,ny_val,uinf_val)
		
		t = Timer(lambda: solve_flow(nx_val,ny_val,dx,dy,u,v,mu_val/rho_val))
		print('total elapsed time: %10.6fs' % t.timeit(number=1))

		post_process(X,Y,u,v,uinf_val)

	except ValueError:
		pass

	      
if __name__ == '__main__':

	try: 
		if sys.argv[1] == 'gui' or sys.argv[1] == '-i':
			root = Tk()
			root.title("Laminar Boundary Layer Solver")

			mainframe = ttk.Frame(root, padding="3 3 12 12")
			mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
			mainframe.columnconfigure(0, weight=1)
			mainframe.rowconfigure(0, weight=1)

			rho = StringVar()
			mu = StringVar()
			uinf = StringVar()
			L = StringVar()
			H = StringVar()
			nx = StringVar()
			ny = StringVar()
			rey = StringVar()
			delta = StringVar()

			ttk.Label(mainframe, text="Flow Parameters").grid(column=1, row=1, sticky=W)
			ttk.Label(mainframe, text="Density").grid(column=1, row=2, sticky=W)
			rho_entry = ttk.Entry(mainframe, width=10, textvariable=rho)
			rho_entry.grid(column=2, row=2, sticky=(W, E))
			
			ttk.Label(mainframe, text="Dyn. Viscosity").grid(column=1, row=3, sticky=W)
			mu_entry = ttk.Entry(mainframe, width=10, textvariable=mu)
			mu_entry.grid(column=2, row=3, sticky=(W, E))

			ttk.Label(mainframe, text="Freestream Velocity").grid(column=1, row=4, sticky=W)
			uinf_entry = ttk.Entry(mainframe, width=10, textvariable=uinf)
			uinf_entry.grid(column=2, row=4, sticky=(W, E))

			ttk.Label(mainframe, text="Problem Parameters").grid(column=4, row=1, sticky=W)
			ttk.Label(mainframe, text="Plate Length").grid(column=4, row=2, sticky=W)
			L_entry = ttk.Entry(mainframe, width=8, textvariable=L)
			L_entry.grid(column=5, row=2, sticky=(W, E))
			
			ttk.Label(mainframe, text="Problem Height").grid(column=4, row=3, sticky=W)
			H_entry = ttk.Entry(mainframe, width=8, textvariable=H)
			H_entry.grid(column=5, row=3, sticky=(W, E))
			
			ttk.Label(mainframe, text="N. of pts along x").grid(column=4, row=4, sticky=W)
			nx_entry = ttk.Entry(mainframe, width=8, textvariable=nx)
			nx_entry.grid(column=5, row=4, sticky=(W, E))
			
			ttk.Label(mainframe, text="N. of pts along y").grid(column=4, row=5, sticky=W)
			ny_entry = ttk.Entry(mainframe, width=8, textvariable=ny)
			ny_entry.grid(column=5, row=5, sticky=(W, E))
			
			#Outputs
			ttk.Label(mainframe, text="Flow Reynolds number:").grid(column=1, row=6, sticky=E)
			ttk.Label(mainframe, width=8, textvariable=rey).grid(column=2, row=6, sticky=(W, E))
			
			ttk.Label(mainframe, text="B. L. Thickness at ").grid(column=4, row=6, sticky=E)
			ttk.Label(mainframe, width=3, textvariable=L).grid(column=5, row=6, sticky=(W, E))
			ttk.Label(mainframe, width=2, text= "= ").grid(column=6, row=6, sticky=(W, E))
			ttk.Label(mainframe, width=6, textvariable=delta).grid(column=7, row=6, sticky=(W, E))

			ttk.Button(mainframe, text="Calculate", command=lambda: calculate()).grid(column=7, row=7, sticky=W)
			
			for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

			rho_entry.focus()
			root.bind('<Return>', calculate)

			root.mainloop()
		else: 
			raise ValueError
	except:
		# Parameters
		rho = 1.; 	##  kg/m^3
		uinf = 1.;   	##  m/s
		mu = 1e-5; 	##  kg/(m*s)
		nu = mu/rho; 	##  m^2/s

		L = 0.2; 	##  m
		H = 0.03; 	##  m
		nx = 161;
		ny = 241;

		dx 	= L/(nx-1);
		dy 	= H/(ny-1);
		x 	= np.linspace(0,L,nx)
		y 	= np.linspace(0,H,ny)
		X,Y 	= np.meshgrid(x,y)
		#[X,Y] = meshgrid(0:dx:L,0:dy:H);
		Re_L 	= uinf*L/nu;
		delta_L = 5./np.sqrt(uinf*L/nu);	## laminar flow
		
		#initial conditions
		u,v = initialize_flat_plate(nx,ny,uinf)
		
		t = Timer(lambda: solve_flow(nx,ny,dx,dy,u,v,nu))
		print('total elapsed time: %10.6fs' % t.timeit(number=1))

		post_process(X,Y,u,v,uinf)
