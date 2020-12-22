# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 06:45:54 2020

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
    theta0: Steering angle
    Nx: The number of elements along x axis
    Ny: The number of elements along y axis
    Nz: The number of elements along z axis
    increaserate: This is the amount of change of distances between the elements in the case of NON-UNIFORM spacing.

NOTE: For general idea about the theory (equations and geometrical configurations (symmetrical and asymmetrical array)), 
please check the 'Theory of Array Factor.pdf'

'''
#%% Function for calculating the array factor

def af_symmetrical_phasescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane):
    c=3e8
    lamda=c/f
    lamda0=c/f0
    
    k=2*pi/lamda
    k0=2*pi/lamda0
    
    ''' 
    This section is all about defining the inter element spacing which depends on lambda and increase rate.
    '''
    #To create an symmetrical array:
    
    if Nx>0:
        distances_along_x=[]
        dx=bx #origin
        for n in range(int(Nx/2)):
            distances_along_x.append(dx)
            dx=dx+increase_rate
        new_list_x=sorted(distances_along_x,reverse=True)
        new_list_x.remove(bx)
        new_list_x.extend(distances_along_x)
        new_list_x.insert(0, 0)    #new_list_x contains the position of each element along x axis
         
    if Ny>0:
        distances_along_y=[]
        dy=by #origin
        for n in range(int(Ny/2)):
            distances_along_y.append(dy)
            dy=dy+increase_rate
        new_list_y=sorted(distances_along_y,reverse=True)
        new_list_y.remove(by)
        new_list_y.extend(distances_along_y)
        new_list_y.insert(0, 0)     #new_list_y contains the position of each element along y axis
    
    if Nz>0:
        distances_along_z=[]
        dz=bz #origin
        for n in range(int(Nz/2)):
            distances_along_z.append(dz)
            dz=dz+increase_rate
        new_list_z=sorted(distances_along_z,reverse=True)
        new_list_z.remove(bz)
        new_list_z.extend(distances_along_z)
        new_list_z.insert(0, 0)   #new_list_z contains the position of each element along z axis

    incoming_angle=np.arange(-180,180,0.2) #define the x-axis(start,stop,step)
    

    array_factor_x=np.zeros(len(incoming_angle)) #create empty array
    array_factor_y=np.zeros(len(incoming_angle)) #create empty array
    array_factor_z=np.zeros(len(incoming_angle)) #create empty array

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
            
            all_received_signals_x=[]
            for n in range(0,Nx):
                
                dist=sum(new_list_x[:n+1])*lamda0
                received_signal_x=cmath.exp(1j*((k*dist*sin(theta[i]*pi/180*cos(phi[i]*pi/180)))-(k0*dist*sin(theta0[i]*pi/180)*cos(phi0[i]*pi/180))))
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
        
        
            all_received_signals_y=[]
            for n in range(0,Ny):
                dist=sum(new_list_y[:n+1])*lamda0
                received_signal_y=cmath.exp(1j*((k*dist*sin(theta[i]*pi/180)*sin(phi[i]*pi/180))-(k0*dist*sin(theta0[i]*pi/180)*sin(phi0[i]*pi/180))))
                all_received_signals_y.append(received_signal_y)
    
            array_factor_y[i]=(abs(sum(all_received_signals_y)))*(1/Ny)
        
        else:
            array_factor_y=int(1)
        
        #%%Array Factor along Z axis
        if Nz>0:
            all_received_signals_z=[]
            for n in range(0,Nz):
                dist=sum(new_list_z[:n+1])*lamda0
                received_signal_z=cmath.exp(1j*((k*dist*cos(theta[i]*pi/180))-(k0*dist*cos(theta0*pi/180))))
                all_received_signals_z.append(received_signal_z)
    
            array_factor_z[i]=(abs(sum(all_received_signals_z)))*(1/Nz)
            
        
        else:
            array_factor_z=int(1)
        
        array_factor=array_factor_x*array_factor_y*array_factor_z

    return incoming_angle,array_factor


'''The lines below this comment can be used to get any plot with respect to the given input variables 
which are bx,by,bz,f,f0,theta0,Nx,Ny,Nz,increase_rate,plane '''

# =============================================================================
# #array_factor_planar_asym (bx,by,bz,f,f0,theta0,Nx,Ny,Nz,increase_rate,plane):
# incoming_angle,array_factor=af_symmetrical_phasescannig(0.5,0.5,0.5,9e9,10e9,20,0,32,0,0,'E')
# incoming_angle,array_factor2=af_symmetrical_phasescannig(0.5,0.5,0.5,10e9,10e9,20,0,32,0,0.05,'E')
# incoming_angle,array_factor3=af_symmetrical_phasescannig(0.5,0.5,0.5,11e9,10e9,20,0,32,0,0.1,'E')
# #%% To get the plot
# array_factor_db=20*(np.log10(abs(array_factor)))
# array_factor_db2=20*(np.log10(abs(array_factor2)))
# array_factor_db3=20*(np.log10(abs(array_factor3)))
# 
# plt.figure(figsize=(12,8))
# plt.plot(incoming_angle,array_factor_db,c='green',label='...')
# plt.plot(incoming_angle,array_factor_db2,c='blue',label='...')
# plt.plot(incoming_angle,array_factor_db3,c='red',label='...')
# plt.ylim(-30,0)
# plt.xlim(-120,120)
# plt.title('Uniform spaced Asymmetric Configuration of Planar Array ')
# 
# plt.xlabel('Incident Angle°',size=12)
# plt.ylabel('Array Factor in dB', size=12)
# plt.legend(loc='best')
# plt.grid('on', linestyle='--',alpha=1)
# 
# 
# #Polar Plot:
# incoming_angle_radian=incoming_angle*pi/180
# 
# plt.figure(figsize=(12,8))
# plt.axes(projection='polar')
# plt.title('Uniform spaced Planar Array',size=16)
# plt.polar(incoming_angle_radian,array_factor,c='red')
# 
# =============================================================================
