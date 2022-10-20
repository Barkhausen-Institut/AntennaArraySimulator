# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 07:30:22 2021

@author: merve.tascioglu@barkhauseninstitut.org
"""

'''
IT IS ENOUGH TO EXECUTE ENTIRE CODES HERE TO OPEN USER INTERFACE.
'''
#%%
'''
These four functions which include the corresponding Array Factor (AF) equations must be imported.
NOTE: For general idea about the theory (equations and geometrical configurations (symmetrical and asymmetrical array)), 
please check the 'Theory of Array Factor.pdf'
'''
from array_factor_equations.arrayfactor_symmetrical_timescanning import af_symmetrical_timescannig
from array_factor_equations.arrayfactor_symmetrical_phasescanning import af_symmetrical_phasescannig
from array_factor_equations.arrayfactor_asym_phasescanning import af_asym_phasescannig
from array_factor_equations.arrayfactor_asym_timescanning import af_asym_timescannig

#%% Essential Libraries:
'''Tkinter is the main library used to create user interface.
    Here a good reference about it and can be found: https://www.geeksforgeeks.org/python-tkinter-tutorial/
'''
import tkinter as tk
from tkinter import *
from scipy import interpolate


import os #required to open Theory of Array Factor.pdf by clicking help button on the interface.
import matplotlib
matplotlib.use('TkAgg')  #required to see figures in the interface.
import matplotlib.pyplot as plt

import numpy as np
from math import pi
from PIL import ImageTk, Image  #required to import figures used in the interface

import tkinter
#%%
''' This first part is solely related to user interface window and its content 
    such as Title, Barkhausen's logo, background color, used figures, etc. '''

# To create the main application window (window refers to the user interface):
window = tk.Tk()
window.title('Array Factor Calculator Developed by Barkhausen Institut')
window.geometry("1500x800")
window.resizable(False, False)
colour='steelblue'
window.configure(bg=colour)
fontsize=(None, 10)

#Help menu
menu = tk.Menu(window)
window.config(menu=menu)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)

def open_description():
    os.startfile('Description of variables.txt')
helpmenu.add_command(label='Description of Variables', command=open_description)

def open_theory():
    os.startfile('Theory of Array Factor.pdf')
helpmenu.add_command(label='Theory of Array Factor', command=open_theory)

# To create main title:
title = tk.Label(text="Array Factor Calculator Developed by Barkhausen Institut", font=('Courier', '16', 'bold'), bg=colour)
title.pack(padx=4, pady=45)

#To import Barkhausen's logo:
img  = Image.open("./images/logo.jpeg")
img = img.resize((180, 90))
photo=ImageTk.PhotoImage(img)
lab=tk.Label(image=photo,bg=colour).place(x=1300,y=15)

#To set window icon as Barkhausen logo (the small icon at the top-left corner of the window) :
window.iconphoto(False, tk.PhotoImage(file=("./images/Barkhausen_logo.jpg")))

#To import the figures related to the array coordinate and array geometry:
img2  = Image.open("./images/array_geometry.png")
img2 = img2.resize((340, 250))
photo2=ImageTk.PhotoImage(img2)
lab=tk.Label(image=photo2, bg=colour).place(x=0,y=50)

img3  = Image.open("./images/Asymmetrical_config.png")
img3 = img3.resize((300, 150))
photo3=ImageTk.PhotoImage(img3)
lab=tk.Label(image=photo3,bg=colour).place(x=20,y=400)

img4  = Image.open("./images/symmetrical_config.png")
img4 = img4.resize((300, 150))
photo4=ImageTk.PhotoImage(img4)
lab=tk.Label(image=photo4,bg=colour).place(x=20,y=580)

# To create titles:
title2 = tk.Label(text="DESIGN 1", font=('Courier', '12', 'bold'), bg=colour).place(x=800, y=95)
title3 = tk.Label(text="DESIGN 2", font=('Courier', '12', 'bold'), bg=colour).place(x=950, y=95)
title3 = tk.Label(text="DESIGN 3", font=('Courier', '12', 'bold'), bg=colour).place(x=1095, y=95)

#%% To create texts (labels) and  entry boxes of the variables on the window:

# To create a frame for variable names and entry boxes for their values.
frame = tk.Frame(window)
frame.pack(side='top')
frame.configure(bg=colour)


#Variables for the calculation:
'''
This part is related to the variables required for the array factor calculation:
    
    b: The coefficient represents the association of distance and wavelength. (d=bλ)
    f: Frequency of the signal sent
    f0: Carrier frequency
    Steering angle: Steering angle
    Nx: The number of elements along x axis
    Ny: The number of elements along y axis
    Nz: The number of elements along z axis
    increaserate: This is the amount of change of distances between the elements in the case of NON-UNIFORM spacing.

'''


# To create text boxes and entry boxes for the variables above.
Variables_name=['dx=bx*λ ⇒  bx:',' dy=by*λ ⇒  by:', 'dz=bz*λ ⇒  bz:',
            'Frequency of Electromagnetic Signal [GHz]:','Center Frequency [GHz]:',
           'Steering Angle [degree °]:',
           'Number of elements along x axis: ' ,'Number of elements along y axis: ',
           'Number of elements along z axis: ','Increase Rate of the Distance Between the Elements (For non-uniform spacing): ',
           ]


# Variables of Design 1:
bx= tk.StringVar()
by= tk.StringVar()
bz= tk.StringVar()

f = tk.StringVar()
f0 = tk.StringVar()
steering_angle = tk.StringVar()
Nx= tk.StringVar()
Ny= tk.StringVar()
Nz= tk.StringVar()
increaserate = tk.StringVar()

Variables_value=[bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increaserate]

row_counter = 0
for i, j in zip((Variables_name), (Variables_value)):
    text = tk.Label(frame, text=i,bg=colour,font=fontsize)
    text.grid(row=row_counter, column=0)
    entry = tk.Entry(frame, width=8, textvariable=j)
    entry.grid(row=row_counter, column=1,pady=5)
    row_counter += 1

# To create buttons for plane, scanning techique and geometrical configuration:
'''
    plane: E plane or H plane
    scanning_tech_ : TTD or Phase Shifting
    geometrical_configuration_ : Uniform, Symmetrical Non-uniform and Asymmetrical Non-uniform spacing
'''
plane_= tk.IntVar()
scanning_tech_=tk.IntVar()
geometrical_configuration_=tk.IntVar()

#location of buttons:
x_location=805
y_location=410

tk.Label(window, text='Plane:', bg=colour,font=fontsize).place(x=x_location-160, y=y_location+10)
text=tk.Radiobutton(window, text='E (y-z plane)', variable=plane_, value=1, bg=colour).place(x=x_location, y=y_location)
text=tk.Radiobutton(window, text='H (x-y plane)', variable=plane_, value=2, bg=colour).place(x=x_location, y=y_location+20)

tk.Label(window, text='Scanning Technique:', bg=colour,font=fontsize).place(x=x_location-160, y=y_location+65)
text=tk.Radiobutton(window, text='Phase Shifting', variable=scanning_tech_, value=1, bg=colour).place(x=x_location, y=y_location+55)
text=tk.Radiobutton(window, text='Time Scannig (TTD)', variable=scanning_tech_, value=2, bg=colour).place(x=x_location, y=y_location+75)

tk.Label(window, text='Geometrical Configuration:', bg=colour,font=fontsize).place(x=x_location-160, y=y_location+135)
text=tk.Radiobutton(window, text='Uniform', variable=geometrical_configuration_, value=1, bg=colour).place(x=x_location, y=y_location+115)
text=tk.Radiobutton(window, text='Asymmetrical Confg.', variable=geometrical_configuration_, value=2, bg=colour).place(x=x_location, y=y_location+135)
text=tk.Radiobutton(window, text='Symmmetrical Confg.', variable=geometrical_configuration_, value=3, bg=colour).place(x=x_location, y=y_location+155)

#%%
''' This part is identical to the part written for design 1 above.'''
#Variables of Design 2
b_2_x = tk.StringVar()
b_2_y = tk.StringVar()
b_2_z = tk.StringVar()

f_2 = tk.StringVar()
f0_2 = tk.StringVar()
steering_angle_2 = tk.StringVar()
Nx_2= tk.StringVar()
Ny_2= tk.StringVar()
Nz_2= tk.StringVar()
increaserate_2 = tk.StringVar()

plane_2= tk.IntVar()
scanning_tech_2=tk.IntVar()
geometrical_configuration_2=tk.IntVar()

Variables_value2=[b_2_x,b_2_y,b_2_z,f_2,f0_2,steering_angle_2,Nx_2,Ny_2,Nz_2,increaserate_2]
row_counter = 0
for i, j in zip((Variables_name), (Variables_value2)):
    text = tk.Label(frame, text=i,bg=colour,font=fontsize)
    text.grid(row=row_counter, column=0)
    entry = tk.Entry(frame, width=8, textvariable=j)
    entry.grid(row=row_counter, column=2,padx=100, pady=5)
    row_counter += 1

text=tk.Radiobutton(window, text='E (y-z plane)', variable=plane_2, value=1, bg=colour).place(x=x_location+150, y=y_location)
text=tk.Radiobutton(window, text='H (x-y plane)', variable=plane_2, value=2, bg=colour).place(x=x_location+150, y=y_location+20)

text=tk.Radiobutton(window, text='Phase Shifting', variable=scanning_tech_2, value=1, bg=colour).place(x=x_location+150, y=y_location+55)
text=tk.Radiobutton(window, text='Time Scannig (TTD)', variable=scanning_tech_2, value=2, bg=colour).place(x=x_location+150, y=y_location+75)

text=tk.Radiobutton(window, text='Uniform', variable=geometrical_configuration_2, value=1, bg=colour).place(x=x_location+150, y=y_location+115)
text=tk.Radiobutton(window, text='Asymmetrical Confg.', variable=geometrical_configuration_2, value=2, bg=colour).place(x=x_location+150, y=y_location+135)
text=tk.Radiobutton(window, text='Symmetrical Confg.', variable=geometrical_configuration_2, value=3, bg=colour).place(x=x_location+150, y=y_location+155)

#%%
''' This part is identical to the part written for design 1 and design 2 above.'''

#Variables of Design 3
b_3_x = tk.StringVar()
b_3_y = tk.StringVar()
b_3_z = tk.StringVar()

f_3 = tk.StringVar()
f0_3 = tk.StringVar()
steering_angle_3 = tk.StringVar()
Nx_3= tk.StringVar()
Ny_3= tk.StringVar()
Nz_3= tk.StringVar()
increaserate_3 = tk.StringVar()

plane_3= tk.IntVar()
scanning_tech_3=tk.IntVar()
geometrical_configuration_3=tk.IntVar()

Variables_value3=[b_3_x,b_3_y,b_3_z,f_3,f0_3,steering_angle_3,Nx_3,Ny_3,Nz_3,increaserate_3]
row_counter = 0
for i, j in zip((Variables_name), (Variables_value3)):
    text = tk.Label(frame, text=i,bg=colour,font=fontsize)
    text.grid(row=row_counter, column=0)
    entry = tk.Entry(frame, width=8, textvariable=j)
    entry.grid(row=row_counter, column=3, pady=5)
    row_counter += 1

text=tk.Radiobutton(window, text='E (y-z plane)', variable=plane_3, value=1, bg=colour).place(x=x_location+300, y=y_location)
text=tk.Radiobutton(window, text='H (x-y plane)', variable=plane_3, value=2, bg=colour).place(x=x_location+300, y=y_location+20)

text=tk.Radiobutton(window, text='Phase Shifting', variable=scanning_tech_3, value=1, bg=colour).place(x=x_location+300, y=y_location+55)
text=tk.Radiobutton(window, text='Time Scannig (TTD)', variable=scanning_tech_3, value=2, bg=colour).place(x=x_location+300, y=y_location+75)

text=tk.Radiobutton(window, text='Uniform', variable=geometrical_configuration_3, value=1, bg=colour).place(x=x_location+300, y=y_location+115)
text=tk.Radiobutton(window, text='Asymmetrical Confg.', variable=geometrical_configuration_3, value=2, bg=colour).place(x=x_location+300, y=y_location+135)
text=tk.Radiobutton(window, text='Symmetrical Confg.', variable=geometrical_configuration_3, value=3, bg=colour).place(x=x_location+300, y=y_location+155)


#%%
'''
This part is all about getting plots by calling the functions written in the scripts imported at the beginning.

'''
#PLOTS:
# Define a function to create the desired plot.
def get_values(event=None):
    # Get these variables from outside the function, and update them.
    global bx,by,bz,f,f0,steering_angle,phi0,Nx,Ny,Nz,increaserate,plane_,scanning_tech_,geometrical_configuration_,b_2_x,b_2_y,b_2_z,f_2,f0_2,steering_angle_2,phi0_2,Nx_2,Ny_2,Nz_2,increaserate_2,plane_2,scanning_tech_2,geometrical_configuration_2,b_3_x,b_3_y,b_3_z,f_3,f0_3,steering_angle_3,phi0_3,Nx_3,Ny_3,Nz_3,increaserate_3,plane_3,scanning_tech_3,geometrical_configuration_3

    try:
        # Convert StringVar data to numerical data.
        b_x = float(bx.get())
        b_y = float(by.get())
        b_z = float(bz.get())

        f_ = float(f.get())*1e9
        f0_ = float(f0.get())*1e9
        steering_angle_= float(steering_angle.get())
        # phi0_ = float(phi0.get())
        Nx_ = int(Nx.get())
        Ny_ = int(Ny.get())
        Nz_ = int(Nz.get())
        increase_rate_ = float(increaserate.get())

        if geometrical_configuration_.get()==1:
            if scanning_tech_.get()==1:
                if plane_.get()==1:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')

        elif geometrical_configuration_.get()==2:
            if scanning_tech_.get()==1:
                if plane_.get()==1:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')


        elif geometrical_configuration_.get()==3:
            if scanning_tech_.get()==1:
                if plane_.get()==1:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_symmetrical_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_symmetrical_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_symmetrical_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor,array_factor_x,array_factor_y,array_factor_z=af_symmetrical_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')

        incoming_angle_radian=incoming_angle*pi/180
        array_factor=array_factor

    except ValueError:
        incoming_angle_radian=0
        array_factor=0
        array_factor_x=0
        array_factor_y=0
        array_factor_z=0

    try:
        b__x = float(b_2_x.get())
        b__y=float(b_2_y.get())
        b__z=float(b_2_z.get())
        f__= float(f_2.get())*1e9
        f0__ = float(f0_2.get())*1e9
        steering_angle__= float(steering_angle_2.get())
        Nx__ = int(Nx_2.get())
        Ny__ = int(Ny_2.get())
        Nz__ = int(Nz_2.get())
        increase_rate__ = float(increaserate_2.get())


        if geometrical_configuration_2.get()==1:
            if scanning_tech_2.get()==1:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')

        elif geometrical_configuration_2.get()==2:
            if scanning_tech_2.get()==1:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')


        elif geometrical_configuration_2.get()==3:
            if scanning_tech_2.get()==1:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_symmetrical_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_symmetrical_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_symmetrical_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2=af_symmetrical_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')

        incoming_angle_radian2=incoming_angle2*pi/180
        array_factor2=array_factor2

    except ValueError:
        incoming_angle_radian2=0
        array_factor2=0
        array_factor_x2=0
        array_factor_y2=0
        array_factor_z2=0

    try:
        b___x = float(b_3_x.get())
        b___y = float(b_3_y.get())
        b___z = float(b_3_z.get())


        f___= float(f_3.get())*1e9
        f0___ = float(f0_3.get())*1e9
        steering_angle___= float(steering_angle_3.get())
        Nx___ = int(Nx_3.get())
        Ny___ = int(Ny_3.get())
        Nz___ = int(Nz_3.get())
        increase_rate___ = float(increaserate_3.get())


        if geometrical_configuration_3.get()==1:
            if scanning_tech_3.get()==1:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')

        elif geometrical_configuration_3.get()==2:
            if scanning_tech_3.get()==1:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')

        elif geometrical_configuration_3.get()==3:
            if scanning_tech_3.get()==1:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_symmetrical_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_symmetrical_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_symmetrical_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=af_symmetrical_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')


        incoming_angle_radian3=incoming_angle3*pi/180
        array_factor3=array_factor3

    except ValueError:
        incoming_angle_radian3=0
        array_factor3=0
        array_factor_x3=0
        array_factor_y3=0
        array_factor_z3=0

    return incoming_angle_radian,incoming_angle_radian2,incoming_angle_radian3,array_factor,array_factor_x,array_factor_y,array_factor_z,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3


    

def default_values_first_design():
    global bx,by,bz,f,f0,steering_angle,phi0,Nx,Ny,Nz,increaserate,plane_,scanning_tech_,geometrical_configuration_

    bx.set(0),by.set(0.5),bz.set(0)
    f.set(10),f0.set(10),steering_angle.set(0),Nx.set(1)
    Ny.set(8),Nz.set(1),increaserate.set(0),geometrical_configuration_.set(1)
    scanning_tech_.set(2),plane_.set(1)

def default_values_other_designs():
    global b_2_x,b_2_y,b_2_z,f_2,f0_2,steering_angle_2,phi0_2,Nx_2,Ny_2,Nz_2,increaserate_2,plane_2,scanning_tech_2,geometrical_configuration_2,b_3_x,b_3_y,b_3_z,f_3,f0_3,steering_angle_3,phi0_3,Nx_3,Ny_3,Nz_3,increaserate_3,plane_3,scanning_tech_3,geometrical_configuration_3

    b_2_x.set(0),b_2_y.set(0.5),b_2_z.set(0)
    f_2.set(10),f0_2.set(10),steering_angle_2.set(0),Nx_2.set(1)
    Ny_2.set(16),Nz_2.set(1),increaserate_2.set(0),geometrical_configuration_2.set(1)
    scanning_tech_2.set(2),plane_2.set(1)

    b_3_x.set(0),b_3_y.set(0.5),b_3_z.set(0)
    f_3.set(10),f0_3.set(10),steering_angle_3.set(0),Nx_3.set(1)
    Ny_3.set(32),Nz_3.set(1),increaserate_3.set(0),geometrical_configuration_3.set(1)
    scanning_tech_3.set(2),plane_3.set(1)


#Fill buttons:
Default_values_first_design = tk.Button(window, command=default_values_first_design, text="Fill Design 1 with default values",font=('Calibri', 10,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'linen').place(x=x_location+450, y=150)
Default_values_all_designs = tk.Button(window, command=default_values_other_designs, text="Fill Design 2&3 with default values",font=('Calibri', 10,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'linen').place(x=x_location+450, y=200)


    
def delete_values():
    global bx,by,bz,f,f0,steering_angle,phi0,Nx,Ny,Nz,increaserate,plane_,scanning_tech_,geometrical_configuration_,b_2_x,b_2_y,b_2_z,f_2,f0_2,steering_angle_2,phi0_2,Nx_2,Ny_2,Nz_2,increaserate_2,plane_2,scanning_tech_2,geometrical_configuration_2,b_3_x,b_3_y,b_3_z,f_3,f0_3,steering_angle_3,phi0_3,Nx_3,Ny_3,Nz_3,increaserate_3,plane_3,scanning_tech_3,geometrical_configuration_3

    for i in bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increaserate,plane_,scanning_tech_,geometrical_configuration_,b_2_x,b_2_y,b_2_z,f_2,f0_2,steering_angle_2,Nx_2,Ny_2,Nz_2,increaserate_2,plane_2,scanning_tech_2,geometrical_configuration_2,b_3_x,b_3_y,b_3_z,f_3,f0_3,steering_angle_3,Nx_3,Ny_3,Nz_3,increaserate_3,plane_3,scanning_tech_3,geometrical_configuration_3:
        i.set('')
        

#Clean buttons:
Delete_all_values = tk.Button(window, command=delete_values, text="Clean values",font=('Calibri', 10,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'linen').place(x=x_location+450, y=250)



def openNewWindow():
    x_location=-110
    y_location=-110
	# be treated as a new window
    newWindow = Toplevel(window)

	# sets the title of the
	# Toplevel widget
    newWindow.title("Simulation Results")

	# sets the geometry of toplevel
    newWindow.geometry("700x500")
    newWindow.iconphoto(False, tk.PhotoImage(file=("./images/Barkhausen_logo.jpg")))

    newWindow.resizable(False, False)
    Label(newWindow,text ="Simulation Results")

    colour='steelblue'
    newWindow.configure(bg=colour)
    fontsize=(None, 10)

    def get_polar_plot():
        
        incoming_angle_radian,incoming_angle_radian2,incoming_angle_radian3,array_factor,array_factor_x,array_factor_y,array_factor_z,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=get_values()
        plt.figure()
        plt.polar(incoming_angle_radian,array_factor,c='blue',label='Design 1')
        plt.polar(incoming_angle_radian2,array_factor2,c='red',label='Design 2')
        plt.polar(incoming_angle_radian3,array_factor3,c='green',label='Design 3')
        plt.legend()
        plt.show()
        
        clicked2.set( "Please select the plot type" )
        runsimulation = tk.Label(newWindow, text=" ",height=15,width = 15,bg=colour).place(x=x_location+140, y=y_location+420)
    
    def get_cartesian_plot():
        incoming_angle_radian,incoming_angle_radian2,incoming_angle_radian3,array_factor,array_factor_x,array_factor_y,array_factor_z,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=get_values()
        
        incoming_angle=incoming_angle_radian*180/pi
        incoming_angle2=incoming_angle_radian2*180/pi
        incoming_angle3=incoming_angle_radian3*180/pi
    
        array_factor_db=20*(np.log10(abs(array_factor)))
        array_factor_db2=20*(np.log10(abs(array_factor2)))
        array_factor_db3=20*(np.log10(abs(array_factor3)))
    
        plt.figure()
        plt.plot(incoming_angle, array_factor_db,c='blue', label='Design 1')
        plt.plot(incoming_angle2, array_factor_db2,c='red',label='Design 2')
        plt.plot(incoming_angle3, array_factor_db3,c='green',label='Design 3')
    
        plt.ylim(-40,0)
        plt.xlim(-100,100)
        plt.xlabel('Incident Angle°',size=12)
        plt.ylabel('Normalized Array Factor in dB', size=12)
        plt.grid('on', linestyle='--',alpha=1)
        plt.legend(loc='best')
        plt.show()
        
    #    runsimulation = tk.Label(newWindow, text=" ",height=15,width = 15,bg=colour).place(x=x_location+140, y=y_location+420)
        clicked2.set( "Please select the plot type" )
        runsimulation = tk.Label(newWindow, text=" ",height=15,width = 15,bg=colour).place(x=x_location+140, y=y_location+420)
    #%% Add buttons to the newwindow:
    hpbw1 = tk.Text(newWindow, height = 1, width = 6)
    hpbw1.place(x=x_location+350, y=55)
    
    hpbw2 = tk.Text(newWindow, height = 1, width = 6)
    hpbw2.place(x=x_location+450, y=55)
    
    hpbw3 = tk.Text(newWindow, height = 1, width = 6)
    hpbw3.place(x=x_location+550, y=55)

    labeldesign1= tk.Label(newWindow,text = "DESIGN 1", font=('Courier', '13', 'bold'), bg=colour).place(x=x_location+340, y=10)
    labeldesign2= tk.Label(newWindow,text = "DESIGN 2", font=('Courier', '13', 'bold'), bg=colour).place(x=x_location+440, y=10)
    labeldesign3= tk.Label(newWindow,text = "DESIGN 3", font=('Courier', '13', 'bold'), bg=colour).place(x=x_location+540, y=10)
#%%
    def hpbwfunctionbroadside(incoming_angle,array_factor_db,steering_angle_1_):
        if isinstance(array_factor_db, np.ndarray):
            condition1=(incoming_angle >steering_angle_1_-90 ) & (steering_angle_1_ < steering_angle_1_+90)
            indices=list((*np.where(condition1)))
            new_x=np.take(incoming_angle, indices)
            arfactr=np.take(array_factor_db,indices,0)
            x=new_x
            y=arfactr
            yToFind = -3
            yreduced = np.array(y) - yToFind
            freduced = interpolate.UnivariateSpline(x, yreduced, s=0)
            thetas=freduced.roots()
            if len(thetas)>0:
#                print(thetas)
#                print(steering_angle_1_)
                difference_array = np.absolute(thetas-steering_angle_1_)
                # find the index of minimum element from the array
                index = difference_array.argmin()
                theta1=thetas[index]
                thetas=np.delete(thetas, index)
                difference_array = np.absolute(thetas-steering_angle_1_)
                # find the index of minimum element from the array
                index = difference_array.argmin()
                theta2=thetas[index]

                try:
                    hpbw_1=np.absolute(theta1-theta2)
                except IndexError:
                    hpbw_1=101.5
            else:
                hpbw_1=101.5
                
        else:
            hpbw_1=101.5
            
        return hpbw_1

    def hpbwfunctionendfire(incoming_angle,array_factor_db,steering_angle_1_):
        if isinstance(array_factor_db, np.ndarray):
            condition1=(incoming_angle >steering_angle_1_-90 ) & (steering_angle_1_ < steering_angle_1_+90)
            indices=list((*np.where(condition1)))
            new_x=np.take(incoming_angle, indices)
            arfactr=np.take(array_factor_db,indices,0)
            #
            x=new_x
            y=arfactr
            yToFind = -3
            yreduced = np.array(y) - yToFind
            freduced = interpolate.UnivariateSpline(x, yreduced, s=0)
            thetas=freduced.roots()
            
            if len(thetas)>0:
                difference_array = np.absolute(thetas-steering_angle_1_)
                # find the index of minimum element from the array
                index = difference_array.argmin()
                theta1=thetas[index]
                thetas=np.delete(thetas, index)
                difference_array = np.absolute(thetas-steering_angle_1_)
                # find the index of minimum element from the array
                index = difference_array.argmin()
                theta2=thetas[index]

                try:
                    hpbw_1=np.absolute(theta1-theta2)
                except IndexError:
                    hpbw_1=46535**(0.5)
            
            else:
                hpbw_1=46535**(0.5)

                
        else:
            hpbw_1=46535**(0.5)
            
        return hpbw_1

#%%    
    def hpbwcalc():
        
        global steering_angle,steering_angle_2,steering_angle_3,hpbw_1,hpbw_2,hpbw_3
    
        incoming_angle_radian,incoming_angle_radian2,incoming_angle_radian3,array_factor,array_factor_x,array_factor_y,array_factor_z,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=get_values()
        
        incoming_angle=incoming_angle_radian*180/pi
        incoming_angle2=incoming_angle_radian2*180/pi
        incoming_angle3=incoming_angle_radian3*180/pi
    
        
        try:
            hpbw1.delete("1.0", tk.END)
            steering_angle_1_= float(steering_angle.get())
           
            array_factor_db=20*(np.log10(abs(array_factor)))
            array_factor_db_x=20*(np.log10(abs(array_factor_x)))
            array_factor_db_y=20*(np.log10(abs(array_factor_y)))
            array_factor_db_z=20*(np.log10(abs(array_factor_z)))
            
            hpbw_1=hpbwfunctionbroadside(incoming_angle,array_factor_db,steering_angle_1_)
            hpbw1.insert(tk.END,hpbw_1)
            
            hpbw_x=hpbwfunctionbroadside(incoming_angle,array_factor_db_x,steering_angle_1_)
            hpbw_y=hpbwfunctionbroadside(incoming_angle,array_factor_db_y,steering_angle_1_)
            hpbw_z=hpbwfunctionendfire(incoming_angle,array_factor_db_z,steering_angle_1_)
    
        except ValueError:# and IndexError:
            hpbw1.insert(tk.END,'')
            hpbw_1=101.5
            hpbw_x=101.5
            hpbw_y=101.5
            hpbw_z=46535
    
        try:
            hpbw2.delete("1.0", tk.END)
            hpbw2.insert(tk.END,'')
            steering_angle_2_= float(steering_angle_2.get())
            
            array_factor_db2=20*(np.log10(abs(array_factor2)))
            array_factor_db_x2=20*(np.log10(abs(array_factor_x2)))
            array_factor_db_y2=20*(np.log10(abs(array_factor_y2)))
            array_factor_db_z2=20*(np.log10(abs(array_factor_z2)))
            
            hpbw_2=hpbwfunctionbroadside(incoming_angle2,array_factor_db2,steering_angle_2_)
            hpbw2.insert(tk.END,hpbw_2)
           
            hpbw_x2=hpbwfunctionbroadside(incoming_angle2,array_factor_db_x2,steering_angle_2_)
            hpbw_y2=hpbwfunctionbroadside(incoming_angle2,array_factor_db_y2,steering_angle_2_)
            hpbw_z2=hpbwfunctionendfire(incoming_angle2,array_factor_db_z2,steering_angle_2_)
        except ValueError:# or IndexError:
            hpbw2.insert(tk.END,'')
            hpbw_2=101.5
            hpbw_x2=101.5
            hpbw_y2=101.5
            hpbw_z2=46535
        
        try:
            hpbw3.delete("1.0",tk.END)
            hpbw3.insert(tk.END,'')
            steering_angle_3_= float(steering_angle_3.get())
    
            array_factor_db3=20*(np.log10(abs(array_factor3)))
            array_factor_db_x3=20*(np.log10(abs(array_factor_x3)))
            array_factor_db_y3=20*(np.log10(abs(array_factor_y3)))
            array_factor_db_z3=20*(np.log10(abs(array_factor_z3)))
           
            hpbw_3=hpbwfunctionbroadside(incoming_angle3,array_factor_db3,steering_angle_3_)
            hpbw3.insert(tk.END,hpbw_3)    
            
            hpbw_x3=hpbwfunctionbroadside(incoming_angle3,array_factor_db_x3,steering_angle_3_)
            hpbw_y3=hpbwfunctionbroadside(incoming_angle3,array_factor_db_y3,steering_angle_3_)
            hpbw_z3=hpbwfunctionendfire(incoming_angle3,array_factor_db_z3,steering_angle_3_)
        except ValueError:# or IndexError:
            hpbw3.insert(tk.END,'')
            hpbw_3=101.5
            hpbw_x3=101.5
            hpbw_y3=101.5
            hpbw_z3=46535
            
        return hpbw_1,hpbw_2,hpbw_3,hpbw_x,hpbw_y,hpbw_z,hpbw_x2,hpbw_y2,hpbw_z2,hpbw_x3,hpbw_y3,hpbw_z3
    
    #
    # HPBW button        
    hpbw_button = tk.Button( newWindow , text = "Calculate HPBW [°]" , command = hpbwcalc,font=('Calibri', 10,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'linen').place(x=15, y=50)
    
    options = ["Normalized Array Factor","Gain Pattern",]
    
    # Dropdown menu options2
    options2 = ["Cartesian Plot","Polar Plot",]
    
    # datatype of menu text
    clicked = tk.StringVar()
    clicked2 = tk.StringVar()
    
    # initial menu text
    clicked.set( "Simulation Results" )
    clicked2.set( "Please select the plot type" )
    
    def arrayfactor_plot_option(name):
        if name=="Cartesian Plot":
            button = tk.Button( newWindow , text = "Get results" , command = get_cartesian_plot,font=('Calibri', 11,'bold'),bg= 'dimgrey', relief=tk.RAISED, borderwidth=4 ).place(x=x_location+140, y=y_location+420)
        elif name=="Polar Plot":
            button = tk.Button( newWindow , text = "Get results" , command = get_polar_plot,font=('Calibri', 11,'bold'),bg= 'dimgrey', relief=tk.RAISED, borderwidth=4 ).place(x=x_location+140, y=y_location+420)
    
        
        
    def directivity_cartesian_plot():
        global bx,by,bz,b_2_x,b_2_y,b_2_z,b_3_x,b_3_y,b_3_z,gain1_value,gain2_value,gain3_value,correction_factor_design1,correction_factor_design2,correction_factor_design3,hpbw_x,hpbw_y,hpbw_z,hpbw_x2,hpbw_y2,hpbw_z2,hpbw_x3,hpbw_y3,hpbw_z3
         
        try:
            bxx= float(bx.get())
            byy= float(by.get())
            bzz= float(bz.get())
        except ValueError:
            bxx=0
            byy=0
            bzz=0
         
        try:
            bxx2= float(b_2_x.get())
            byy2= float(b_2_y.get())
            bzz2= float(b_2_z.get())
       
        except ValueError:
            bxx2=0
            byy2=0
            bzz2=0
        
        try:
            bxx3= float(b_3_x.get())
            byy3= float(b_3_y.get())
            bzz3= float(b_3_z.get())
        except ValueError:
            bxx3=0
            byy3=0
            bzz3=0
    
        if bxx>=1 or byy>=1 or bzz>=1 or bxx2>=1 or byy2>=1 or bzz2>=1 or bxx3>=1 or byy3>=1 or bzz3>=1:
            msg = 'b=d/λ must be smaller than 1 !!!'
            messagebox.showinfo('message', msg)
    
            
        else:
            hpbw_1,hpbw_2,hpbw_3,hpbw_x,hpbw_y,hpbw_z,hpbw_x2,hpbw_y2,hpbw_z2,hpbw_x3,hpbw_y3,hpbw_z3=hpbwcalc()
        
            incoming_angle_radian,incoming_angle_radian2,incoming_angle_radian3,array_factor,array_factor_x,array_factor_y,array_factor_z,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=get_values()
    
            gain1_value,gain2_value,gain3_value,correction_factor_design1,correction_factor_design2,correction_factor_design3=directivity_part("Gain Pattern")
           
            try:
                single_gain1=float(gain1_value)-float(correction_factor_design1)
            except ValueError:
                single_gain1=-float(correction_factor_design1)
            
            try:
                single_gain2=float(gain2_value)-float(correction_factor_design2)
            except ValueError:
                single_gain2=-float(correction_factor_design2)
            try:
                single_gain3=float(gain3_value)-float(correction_factor_design3)
            except ValueError:
                single_gain3=-float(correction_factor_design3)
            
            try:
                incoming_angle=incoming_angle_radian*180/pi
                
                array_factorx_db=10*(np.log10(abs(101.5/hpbw_x)))
                array_factory_db=10*(np.log10(abs(101.5/hpbw_y)))
                array_factorz_db=10*(np.log10(abs(46535/(hpbw_z**2))))
        
                array_directivity_db=(20*(np.log10(abs(array_factor))))+array_factorx_db+array_factory_db+array_factorz_db+single_gain1
                directivity1=str(round(((array_factorx_db+array_factory_db+array_factorz_db)+single_gain1),2))

            except ZeroDivisionError:
                incoming_angle=0
                array_directivity_db=0
                directivity1=str(0)
                hpbw_x=101.5
                hpbw_y=101.5
                hpbw_z=46535**0.5
                
            try:
                incoming_angle2=incoming_angle_radian2*180/pi
        
                array_factorx2_db=10*(np.log10(abs(101.5/hpbw_x2)))
                array_factory2_db=10*(np.log10(abs(101.5/hpbw_y2)))
                array_factorz2_db=10*(np.log10(abs(46535/(hpbw_z2**2))))
        
                array_directivity_db2=(20*(np.log10(abs(array_factor2))))+array_factorx2_db+array_factory2_db+array_factorz2_db+single_gain2
                directivity2=str(round(((array_factorx2_db+array_factory2_db+array_factorz2_db)+single_gain2),2))
            except ZeroDivisionError:
                incoming_angle2=0
                array_directivity_db2=0
                directivity2=str(0)
                hpbw_x2=101.5
                hpbw_y2=101.5
                hpbw_z2=46535**0.5

            try:
                incoming_angle3=incoming_angle_radian3*180/pi
        
                array_factorx3_db=10*(np.log10(abs(101.5/hpbw_x3)))
                array_factory3_db=10*(np.log10(abs(101.5/hpbw_y3)))
                array_factorz3_db=10*(np.log10(abs(46535/(hpbw_z2**2))))
        
                array_directivity_db3=(20*(np.log10(abs(array_factor3))))+array_factorx3_db+array_factory3_db+array_factorz3_db+single_gain3
                directivity3=str(round(((array_factorx3_db+array_factory3_db+array_factorz3_db)+single_gain3),2))
      
            except ZeroDivisionError:
                incoming_angle3=0
                array_directivity_db3=0
                directivity3=str(0)
                hpbw_x3=101.5
                hpbw_y3=101.5
                hpbw_z3=46535**0.5
        
        
            yaxis=max((float(directivity1),float(directivity2),float(directivity3)))
        
        
            plt.figure()
        
            
            if float(directivity1)>single_gain1:
                
                plt.plot(incoming_angle, array_directivity_db,c='blue', label=r'Design 1: peak Gain: {} $ dB$'.format(directivity1))
            else: 
                plt.plot(incoming_angle, array_directivity_db,c='blue', label='')
         
            if float(directivity2)>single_gain2:
                
                plt.plot(incoming_angle2, array_directivity_db2,c='red',label=r'Design 2: peak Gain: {} $ dB$'.format(directivity2))
           
            else:
                plt.plot(incoming_angle2, array_directivity_db2,c='blue', label='')
           
            if float(directivity3)>single_gain3:
                plt.plot(incoming_angle3, array_directivity_db3,c='green',label=r'Design 3: peak Gain: {} $ dB$'.format(directivity3))
            else:
                plt.plot(incoming_angle3, array_directivity_db3,c='blue', label='')
        
           
            plt.ylim(-40,yaxis+5)
            plt.xlim(-100,100)
            plt.xlabel('Incident Angle°',size=12)
            plt.ylabel('Gain in dB', size=12)
            plt.grid('on', linestyle='--',alpha=1)
            plt.legend(loc='best')
            plt.show()
            
            clicked2.set( "Please select the plot type" )
            runsimulation = tk.Label(newWindow, text=" ",height=15,width = 15,bg=colour).place(x=x_location+140, y=y_location+420)
           
        
    def directivity_plot_option(name):
        if name=="Cartesian Plot":
            button = tk.Button( newWindow , text = "Get results" , command = directivity_cartesian_plot,font=('Calibri', 11,'bold'),bg= 'dimgrey', relief=tk.RAISED, borderwidth=4 ).place(x=x_location+140, y=y_location+420)
        elif name=="Polar Plot":
            button = tk.Button( newWindow , text = "Get results" , command = directivity_polar_plot,font=('Calibri', 11,'bold'),bg= 'dimgrey', relief=tk.RAISED, borderwidth=4 ).place(x=x_location+140, y=y_location+420)
    
    
    gain1 =tk.StringVar()
    gain2 =tk.StringVar()
    gain3 =tk.StringVar()

    losses_design1=tk.StringVar()
    losses_design2=tk.StringVar()
    losses_design3=tk.StringVar()
    
    
    def directivity_part(x):   
        global Single_directivity#,correction_factor_design1,correction_factor_design2,correction_factor_design3
        
        if x == "Gain Pattern":
            Single_directivity= tk.Label(newWindow,text = "Gain of the single antenna (in dB) :",font=('Calibri', 10,'bold')).place(x=x_location+125, y=y_location+290)
           
            entry1 = Entry(newWindow,textvariable=gain1,width=8)
            entry1.place(x=x_location+350, y=y_location+290)
            gain1_value=entry1.get()

            entry12 = Entry(newWindow,textvariable=gain2,width=8)
            entry12.place(x=x_location+450, y=y_location+290)
            gain2_value=entry12.get()

            entry13 = Entry(newWindow,textvariable=gain3,width=8)
            entry13.place(x=x_location+550, y=y_location+290)
            gain3_value=entry13.get()

            label_correctionfactor= tk.Label(newWindow,text = "Losses (in dB) :",font=('Calibri', 10,'bold')).place(x=x_location+125, y=y_location+250)
            
            entry2 = Entry(newWindow,textvariable=losses_design1,width=8)
            entry2.place(x=x_location+350, y=y_location+250)
            
            entry3 = Entry(newWindow,textvariable=losses_design2,width=8)
            entry3.place(x=x_location+450, y=y_location+250)
            
            entry4 = Entry(newWindow,textvariable=losses_design3,width=8)
            entry4.place(x=x_location+550, y=y_location+250)

            entry4 = Entry(newWindow,textvariable=losses_design3,width=8)
            entry4.place(x=x_location+550, y=y_location+250)

            if not losses_design1.get():
                correction_factor_design1=0
            else:
                correction_factor_design1=entry2.get()

           
            if not losses_design2.get():
                correction_factor_design2=0
            else:
                correction_factor_design2=entry3.get()
                

            if not losses_design3.get():
                correction_factor_design3=0
            else:
                correction_factor_design3=entry4.get()
            
            
            dropmenu2 = tk.OptionMenu( newWindow , clicked2 , *options2,command=directivity_plot_option).place(x=x_location+125, y=y_location+330)
            
        else:
            entries_delete = tk.Label(newWindow, text="",width = 100,height=10,bg=colour).place(x=x_location+125, y=y_location+250)
            
            clicked2.set( "Please select the plot type" )
            dropmenu2 = tk.OptionMenu( newWindow , clicked2 , *options2,command=arrayfactor_plot_option).place(x=x_location+125, y=y_location+330)
        
        return gain1_value,gain2_value,gain3_value,correction_factor_design1,correction_factor_design2,correction_factor_design3
        
    dropmenu1 = tk.OptionMenu(newWindow, clicked, *options,command=directivity_part).place(x=x_location+125, y=y_location+210)
    
    
    
    
    def directivity_polar_plot():
        global bx,by,bz,b_2_x,b_2_y,b_2_z,b_3_x,b_3_y,b_3_z,gain1_value,gain2_value,gain3_value,correction_factor_design1,correction_factor_design2,correction_factor_design3,hpbw_x,hpbw_y,hpbw_z,hpbw_x2,hpbw_y2,hpbw_z2,hpbw_x3,hpbw_y3,hpbw_z3
         
        try:
            bxx= float(bx.get())
            byy= float(by.get())
            bzz= float(bz.get())
        except ValueError:
            bxx=0
            byy=0
            bzz=0
         
        try:
            bxx2= float(b_2_x.get())
            byy2= float(b_2_y.get())
            bzz2= float(b_2_z.get())
       
        except ValueError:
            bxx2=0
            byy2=0
            bzz2=0
        
        try:
            bxx3= float(b_3_x.get())
            byy3= float(b_3_y.get())
            bzz3= float(b_3_z.get())
        except ValueError:
            bxx3=0
            byy3=0
            bzz3=0
    
        if bxx>=1 or byy>=1 or bzz>=1 or bxx2>=1 or byy2>=1 or bzz2>=1 or bxx3>=1 or byy3>=1 or bzz3>=1:
            msg = 'b=d/λ must be smaller than 1 !!!'
            messagebox.showinfo('message', msg)
    
            
        else:
            hpbw_1,hpbw_2,hpbw_3,hpbw_x,hpbw_y,hpbw_z,hpbw_x2,hpbw_y2,hpbw_z2,hpbw_x3,hpbw_y3,hpbw_z3=hpbwcalc()
        
            incoming_angle_radian,incoming_angle_radian2,incoming_angle_radian3,array_factor,array_factor_x,array_factor_y,array_factor_z,array_factor2,array_factor_x2,array_factor_y2,array_factor_z2,array_factor3,array_factor_x3,array_factor_y3,array_factor_z3=get_values()
            
            
            gain1_value,gain2_value,gain3_value,correction_factor_design1,correction_factor_design2,correction_factor_design3=directivity_part("Gain Pattern")
            try:
                single_gain1=float(gain1_value)-float(correction_factor_design1)
            except ValueError:
                single_gain1=-float(correction_factor_design1)
            
            try:
                single_gain2=float(gain2_value)-float(correction_factor_design2)
            except ValueError:
                single_gain2=-float(correction_factor_design2)
            try:
                single_gain3=float(gain3_value)-float(correction_factor_design3)
            except ValueError:
                single_gain3=-float(correction_factor_design3)
            
            try:
                incoming_angle=incoming_angle_radian*180/pi
                
                array_factorx_db=10*(np.log10(abs(101.5/hpbw_x)))
                array_factory_db=10*(np.log10(abs(101.5/hpbw_y)))
                array_factorz_db=10*(np.log10(abs(46535/(hpbw_z**2))))
        
                array_directivity_db=(20*(np.log10(abs(array_factor))))+array_factorx_db+array_factory_db+array_factorz_db+single_gain1
                directivity1=str(round(((array_factorx_db+array_factory_db+array_factorz_db)+single_gain1),2))
                
            except ZeroDivisionError:
                incoming_angle=0
                array_directivity_db=0
                directivity1=str(0)
                hpbw_x=101.5
                hpbw_y=101.5
                hpbw_z=46535**0.5
                
            try:
                incoming_angle2=incoming_angle_radian2*180/pi
                array_factorx2_db=10*(np.log10(abs(101.5/hpbw_x2)))
                array_factory2_db=10*(np.log10(abs(101.5/hpbw_y2)))
                array_factorz2_db=10*(np.log10(abs(46535/(hpbw_z2**2))))
        
                array_directivity_db2=(20*(np.log10(abs(array_factor2))))+array_factorx2_db+array_factory2_db+array_factorz2_db+single_gain2
                directivity2=str(round(((array_factorx2_db+array_factory2_db+array_factorz2_db)+single_gain2),2))
        
        
            except ZeroDivisionError:
                incoming_angle2=0
                array_directivity_db2=0
                directivity2=str(0)
                hpbw_x2=101.5
                hpbw_y2=101.5
                hpbw_z2=46535**0.5
            try:
                incoming_angle3=incoming_angle_radian3*180/pi
        
                array_factorx3_db=10*(np.log10(abs(101.5/hpbw_x3)))
                array_factory3_db=10*(np.log10(abs(101.5/hpbw_y3)))
                array_factorz3_db=10*(np.log10(abs(46535/(hpbw_z3**2))))
        
                array_directivity_db3=(20*(np.log10(abs(array_factor3))))+array_factorx3_db+array_factory3_db+array_factorz3_db+single_gain3
                directivity3=str(round(((array_factorx3_db+array_factory3_db+array_factorz3_db)+single_gain3),2))
        
            except ZeroDivisionError:
                incoming_angle3=0
                array_directivity_db3=0
                directivity3=str(0)
                hpbw_x3=101.5
                hpbw_y3=101.5
                hpbw_z3=46535**0.5
        
        
            plt.figure()
        
        
            if float(directivity1)>single_gain1:
                plt.polar(incoming_angle_radian, (10**(array_directivity_db/20)),c='blue', label=r'max. Directivity: {} $ dB$'.format(directivity1))
            else: 
                plt.polar(incoming_angle, array_directivity_db,c='blue', label='')
         
            if float(directivity2)>single_gain2:
                
                plt.polar(incoming_angle_radian2, (10**(array_directivity_db2/20)),c='red',label=r'max. Directivity: {} $ dB$'.format(directivity2))
           
            else:
                plt.polar(incoming_angle2, array_directivity_db2,c='blue', label='')
           
            if float(directivity3)>single_gain3:
                
                plt.polar(incoming_angle_radian3, (10**(array_directivity_db3/20)),c='green',label=r'max. Directivity: {} $ dB$'.format(directivity3))
            else:
                plt.polar(incoming_angle3, array_directivity_db3,c='blue', label='')

            plt.show()
        
            clicked2.set( "Please select the plot type" )
            runsimulation = tk.Label(newWindow, text=" ",height=15,width = 15,bg=colour).place(x=x_location+140, y=y_location+420)




# a button widget which will open a
# new window on button click
btn = Button(window,text ="Run Simulation",command = openNewWindow,font=('Calibri', 10,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'linen').place(x=x_location+150, y=y_location+230)



# Execute tkinter
window.mainloop()

