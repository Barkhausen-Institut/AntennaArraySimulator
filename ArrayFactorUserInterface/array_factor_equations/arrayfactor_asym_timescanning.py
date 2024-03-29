# -*- coding: utf-8 -*-
"""
Created on Mon Aug Sep 08:43:32 2020

@author:merve.tascioglu@barkhauseninstitut.org
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

def af_asym_timescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane):
    
    ''' 
    This section is all about defining the inter element spacing which depends on lambda and increase rate.
    '''
  
    #To create an asymmetrical array:
    if Nx>0:
        distances_along_x=[0]
        dx=0 #origin
        for n in range(0,Nx-1):
            dx=dx+(bx+(n*increase_rate))
            distances_along_x.append(dx)   #distances_along_x contains the position of each element along x axis
            
    if Ny>0:
        distances_along_y=[0]
        dy=0 #origin
        for n in range(0,Ny-1):
            dy=dy+(by+(n*increase_rate))
            distances_along_y.append(dy)   #distances_along_y contains the position of each element along y axis
    
    if Nz>0:
        distances_along_z=[0]
        dz=0 #origin
        for n in range(0,Nz-1):
            dz=dz+(bz+(n*increase_rate))
            distances_along_z.append(dz)  #distances_along_z contains the position of each element along z axis
        
    c=3e8
    lamda=c/f
    lamda0=c/f0
    k=2*pi/lamda
    

    incoming_angle=np.arange(-180,180,0.2) #define the x-axis of the plot.

    array_factor_x=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below
    array_factor_y=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below
    array_factor_z=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below

    for i in range(len(incoming_angle)):
        
        #%%Array Factor along X axis
        if Nx>0:
            # Based on the plane, either phi or theta must be kept constant. 
            if plane=='E':
                phi=np.zeros(len(incoming_angle)) 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                # theta=np.transpose(theta)
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
            
            phase_function_x=(sin(theta[i]*pi/180)*cos(phi[i]*pi/180))-sin(theta0[i]*pi/180)*cos(phi0[i]*pi/180)

            all_received_signals_x=[]
            for n in range(0,Nx):
                
                dist=distances_along_x[n]*lamda0
                received_signal_x=cmath.exp(1j*k*dist*phase_function_x)
                all_received_signals_x.append(received_signal_x)
                
            array_factor_x[i]=(abs(sum(all_received_signals_x)))*(1/Nx)
        else:
            array_factor_x=int(1)
        
        if Ny>0:
        #%%Array Factor along Y axis
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
        
            phase_function_y=(sin(theta[i]*pi/180)*sin(phi[i]*pi/180))-(sin(theta0[i]*pi/180)*sin(phi0[i]*pi/180))
            all_received_signals_y=[]
            for n in range(0,Ny):
                
                dist=distances_along_y[n]*lamda0
                received_signal_y=cmath.exp(1j*k*dist*phase_function_y)
                all_received_signals_y.append(received_signal_y)
    
            array_factor_y[i]=(abs(sum(all_received_signals_y)))*(1/Ny)
        
        else:
            array_factor_y=int(1)
        
        #%%Array Factor along Z axis
        if Nz>0:
            theta=incoming_angle
            theta0=np.ones(len(incoming_angle))*steering_angle

            phase_function_z=cos(theta[i]*pi/180)-cos(theta0[i]*pi/180)
            all_received_signals_z=[]
            for n in range(0,Nz):
                
                dist=distances_along_z[n]*lamda0
                received_signal_z=cmath.exp(1j*k*dist*phase_function_z)
                all_received_signals_z.append(received_signal_z)
    
            array_factor_z[i]=(abs(sum(all_received_signals_z)))*(1/Nz)
            
        
        else:
            array_factor_z=int(1)
        
        array_factor=array_factor_x*array_factor_y*array_factor_z

    return incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z



'''The lines below this comment can be used to get any plot with respect to the given input variables 
which are bx,by,bz,f,f0,theta0,Nx,Ny,Nz,increase_rate,plane '''


# =============================================================================
# #af_asym_timescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane)
# theta_incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_timescannig(0.5,0,0,10e9,10e9,0,0,4,0,0,'E')
# 
# 
# 
# #%% To get the plot
# array_factor_db_1=20*(np.log10(abs(array_factor)))
# 
# #
# plt.figure(figsize=(12,8))
# plt.plot(theta_incoming_angle,array_factor_db_1,c='k',label='....')
# plt.plot(theta_incoming_angle,array_factor_db_2,c='k',label='....')
# plt.ylim(-40,0)
# plt.xlim(-80,80)
# plt.title('Uniform spaced Asymmetric Configuration of Planar Array ')
# 
# plt.xlabel('Incident Angle°',size=12)
# plt.ylabel('Array Factor in dB', size=12)
# plt.legend(loc='best')
# plt.grid('on', linestyle='--',alpha=1)
# 
# # np.interp(0, theta_incoming_angle,array_factor_db)
# 
# #Polar
# theta_incoming_angle_radian=theta_incoming_angle*pi/180
# 
# plt.figure(figsize=(12,8))
# plt.axes(projection='polar')
# plt.title('Uniform spaced Planar Array',size=16)
# plt.polar(theta_incoming_angle_radian,array_factor,c='red')
# 
# =============================================================================
