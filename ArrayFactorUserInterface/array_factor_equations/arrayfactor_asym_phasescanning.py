# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 07:30:14 2020

@author: merve.tascioglu@barkhauseninstitut.org
"""

from math import sin,pi,log,cos
import cmath
import numpy as np
import matplotlib.pyplot as plt


''' Before examining the code below, let's describe the input variables that are required for AF calculatin.
    
    b: The coefficient represents the association of distance and wavelength. (d=bλ)
    f: Frequency of the signal sent
    f0: Carrier frequency
    steering_angle: Steering angle
    Nx: The number of elements along x axis
    Ny: The number of elements along y axis
    Nz: The number of elements along z axis
    increaserate: This is the amount of change of distances between the elements in the case of NON-UNIFORM spacing.

NOTE: For general idea about the theory (equations and geometrical configurations (symmetrical and asymmetrical array)), 
please check the 'Theory of Array Factor.pdf'

'''
#%% Function for calculating the array factor

def af_asym_phasescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane):
    
    c=3e8
    lamda=c/f   
    lamda0=c/f0
    
    k=2*pi/lamda
    k0=2*pi/lamda0
    
    #%%
    ''' 
    This section is all about defining the inter element spacing which depends on lambda and increase rate.
    '''
    #To create an asymmetrical array:
    if Nx>0:
        distances_along_x=[0]
        dx=0 #origin
        for n in range(0,Nx-1):
            dx=dx+(bx+(n*increase_rate))
            distances_along_x.append(dx*lamda0)  #distances_along_x contains the position of each element along x axis
            
    if Ny>0:
        distances_along_y=[0]
        dy=0 #origin
        for n in range(0,Ny-1):
            dy=dy+(by+(n*increase_rate))
            distances_along_y.append(dy*lamda0)  #distances_along_y contains the position of each element along y axis
    
    if Nz>0:
        distances_along_z=[0]
        dz=0 #origin
        for n in range(0,Nz-1):
            dz=dz+(bz+(n*increase_rate))
            distances_along_z.append(dz*lamda0)  #distances_along_z contains the position of each element along z axis
        
    #%%

    incoming_angle=np.arange(-180,180,0.2) # To define the x-axis of plot (incoming angle,theta)
    

    array_factor_x=np.zeros(len(incoming_angle)) #to create an empty array which will be filled via for loop below with respect to the incoming angle, theta.
    array_factor_y=np.zeros(len(incoming_angle)) #to create an empty array which will be filled via for loop below with respect to the incoming angle, theta.
    array_factor_z=np.zeros(len(incoming_angle)) #to create an empty array which will be filled via for loop below with respect to the incoming angle, theta.

    for i in range(len(incoming_angle)):
        
        #%%
        ''' This section is all about the implementation of the equations come about the theory.
        To clarify these equations, please check the 'Theory of Array Factor.pdf'.
        '''
        #Array Factor along X axis
        if Nx>0:
            
            # Based on the plane, either phi or theta must be kept constant. 
            if plane=='E':
                phi=np.zeros(len(incoming_angle)) 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle

            all_received_signals_x=[]
            for n in range(0,Nx):
                
                dist=distances_along_x[n]
                received_signal_x=cmath.exp(1j*((k*dist*sin(theta[i]*pi/180*cos(phi[i]*pi/180)))-(k0*dist*sin(theta0[i]*pi/180)*cos(phi0[i]*pi/180))))
                all_received_signals_x.append(received_signal_x)
                
            array_factor_x[i]=(abs(sum(all_received_signals_x)))*(1/Nx)
        else:
            array_factor_x=int(1)
        
        
        #%%Array Factor along Y axis
        if Ny>0:
        # Based on the plane, either phi or theta must be kept constant. 
            if plane=='E':
                phi=np.ones(len(incoming_angle))*90 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
        

            all_received_signals_y=[]
            for n in range(0,Ny):
                dist=distances_along_y[n]
                received_signal_y=cmath.exp(1j*((k*dist*sin(theta[i]*pi/180)*sin(phi[i]*pi/180))-(k0*dist*sin(theta0[i]*pi/180)*sin(phi0[i]*pi/180))))
                all_received_signals_y.append(received_signal_y)
    
            array_factor_y[i]=(abs(sum(all_received_signals_y)))*(1/Ny)
        
        else:
            array_factor_y=int(1)
        
        #%%Array Factor along Z axis
        if Nz>0:
            all_received_signals_z=[]
            for n in range(0,Nz):
                dist=distances_along_z[n]
                received_signal_z=cmath.exp(1j*((k*dist*cos(incoming_angle[i]*pi/180))-(k0*dist*cos(steering_angle*pi/180))))
                all_received_signals_z.append(received_signal_z)
            array_factor_z[i]=(abs(sum(all_received_signals_z)))*(1/Nz)
        else:
            array_factor_z=int(1)
        array_factor=array_factor_x*array_factor_y*array_factor_z

    return incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z

'''The lines below this comment can be used to get any plot with respect to the given input variables 
which are bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane '''

# =============================================================================
# #%%
# #af_asym_phasescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane):
#incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_phasescannig(0.5,0.5,0.5,9e9,10e9,20,0,32,0,0,'E')
# incoming_angle,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_phasescannig(0.5,0.5,0.5,10e9,10e9,20,0,32,0,0,'E')
# incoming_angle,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_phasescannig(0.5,0.5,0.5,11e9,10e9,20,0,32,0,0,'E')
# 
# 
# #%% To get the cartesian plot
# 
# array_factor_db=20*(np.log10(abs(array_factor)))
# array_factor_db2=20*(np.log10(abs(array_factor2)))
# array_factor_db3=20*(np.log10(abs(array_factor3)))
# 
# 
# plt.figure(figsize=(12,8))
# plt.plot(incoming_angle,array_factor_db,c='green',label='...')
# plt.plot(incoming_angle,array_factor_db2,c='blue',label='...')
# plt.plot(incoming_angle,array_factor_db3,c='red',label='...')
# 
# plt.ylim(-30,0)
# plt.xlim(0,40)
# plt.title('Uniform spaced Asymmetric Configuration of Planar Array ')
# 
# plt.xlabel('Incident Angle°',size=12)
# plt.ylabel('Array Factor in dB', size=12)
# plt.legend(loc='best')
# plt.grid('on', linestyle='--',alpha=1)
# 
# 
# # To get the Polar plot 
# incoming_angle_radian=incoming_angle*pi/180
# 
# plt.figure(figsize=(12,8))
# plt.axes(projection='polar')
# plt.title('Uniform spaced Planar Array',size=16)
# plt.polar(incoming_angle_radian,array_factor,c='red')
# #plt.polar(incoming_angle,array_factor_numpy)
# # 
# 
# =============================================================================


