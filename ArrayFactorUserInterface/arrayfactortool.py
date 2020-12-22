# -*- coding: utf-8 -*-
"""
Created on Mon Nov 2 07:30:22 2020

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
img  = Image.open("./images/Barkhausen.jpg")
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
y_location=430

tk.Label(window, text='Plane:', bg=colour,font=fontsize).place(x=x_location-160, y=y_location+10)
text=tk.Radiobutton(window, text='E (y-z plane)', variable=plane_, value=1, bg=colour).place(x=x_location, y=y_location)
text=tk.Radiobutton(window, text='H (x-y plane)', variable=plane_, value=2, bg=colour).place(x=x_location, y=y_location+20)

tk.Label(window, text='Scanning Technique:', bg=colour,font=fontsize).place(x=x_location-160, y=y_location+70)
text=tk.Radiobutton(window, text='Phase Shifting', variable=scanning_tech_, value=1, bg=colour).place(x=x_location, y=y_location+60)
text=tk.Radiobutton(window, text='Time Scannig (TTD)', variable=scanning_tech_, value=2, bg=colour).place(x=x_location, y=y_location+80)

tk.Label(window, text='Geometrical Configuration:', bg=colour,font=fontsize).place(x=x_location-160, y=y_location+140)
text=tk.Radiobutton(window, text='Uniform', variable=geometrical_configuration_, value=1, bg=colour).place(x=x_location, y=y_location+120)
text=tk.Radiobutton(window, text='Asymmetrical Confg.', variable=geometrical_configuration_, value=2, bg=colour).place(x=x_location, y=y_location+140)
text=tk.Radiobutton(window, text='Symmmetrical Confg.', variable=geometrical_configuration_, value=3, bg=colour).place(x=x_location, y=y_location+160)

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

text=tk.Radiobutton(window, text='Phase Shifting', variable=scanning_tech_2, value=1, bg=colour).place(x=x_location+150, y=y_location+60)
text=tk.Radiobutton(window, text='Time Scannig (TTD)', variable=scanning_tech_2, value=2, bg=colour).place(x=x_location+150, y=y_location+80)

text=tk.Radiobutton(window, text='Uniform', variable=geometrical_configuration_2, value=1, bg=colour).place(x=x_location+150, y=y_location+120)
text=tk.Radiobutton(window, text='Asymmetrical Confg.', variable=geometrical_configuration_2, value=2, bg=colour).place(x=x_location+150, y=y_location+140)
text=tk.Radiobutton(window, text='Symmetrical Confg.', variable=geometrical_configuration_2, value=3, bg=colour).place(x=x_location+150, y=y_location+160)

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

text=tk.Radiobutton(window, text='Phase Shifting', variable=scanning_tech_3, value=1, bg=colour).place(x=x_location+300, y=y_location+60)
text=tk.Radiobutton(window, text='Time Scannig (TTD)', variable=scanning_tech_3, value=2, bg=colour).place(x=x_location+300, y=y_location+80)

text=tk.Radiobutton(window, text='Uniform', variable=geometrical_configuration_3, value=1, bg=colour).place(x=x_location+300, y=y_location+120)
text=tk.Radiobutton(window, text='Asymmetrical Confg.', variable=geometrical_configuration_3, value=2, bg=colour).place(x=x_location+300, y=y_location+140)
text=tk.Radiobutton(window, text='Symmetrical Confg.', variable=geometrical_configuration_3, value=3, bg=colour).place(x=x_location+300, y=y_location+160)


#%%
'''
This part is all about getting plots by calling the functions written in the scripts imported at the beginning.

'''

#PLOTS:
# Define a function to create the desired plot.
def make_cartesian_plot(event=None):
    # Get these variables from outside the function, and update them.
    global bx,by,bz,f,f0,steering_angle,phi0,Nx,Ny,Nz,increaserate,plane_,scanning_tech_,geometrical_configuration_,b_2_x,b_2_y,b_2_z,f_2,f0_2,steering_angle_2,Nx_2,Ny_2,Nz_2,increaserate_2,plane_2,scanning_tech_2,geometrical_configuration_2,b_3_x,b_3_y,b_3_z,f_3,f0_3,steering_angle_3,Nx_3,Ny_3,Nz_3,increaserate_3,plane_3,scanning_tech_3,geometrical_configuration_3

    try:

        # Convert StringVar data to numerical data.
        b_x = float(bx.get())
        b_y = float(by.get())
        b_z = float(bz.get())

        f_ = float(f.get())*1e9
        f0_ = float(f0.get())*1e9
        steering_angle_= float(steering_angle.get())
        Nx_ = int(Nx.get())
        Ny_ = int(Ny.get())
        Nz_ = int(Nz.get())
        increase_rate_ = float(increaserate.get())

        if geometrical_configuration_.get()==1:
            if scanning_tech_.get()==1:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')

        elif geometrical_configuration_.get()==2:
            if scanning_tech_.get()==1:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')


        elif geometrical_configuration_.get()==3:
            if scanning_tech_.get()==1:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_symmetrical_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_symmetrical_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_symmetrical_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_symmetrical_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')

        array_factor_db=20*(np.log10(abs(array_factor)))
        incoming_angle=incoming_angle

    except ValueError:
        incoming_angle=0
        array_factor_db=0


    try:
        b__x = float(b_2_x.get())
        b__y = float(b_2_y.get())
        b__z = float(b_2_z.get())


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
                    incoming_angle2,array_factor2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')

        elif geometrical_configuration_2.get()==2:
            if scanning_tech_2.get()==1:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')


        elif geometrical_configuration_2.get()==3:
            if scanning_tech_2.get()==1:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_symmetrical_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_symmetrical_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_symmetrical_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_symmetrical_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')

        array_factor_db2=20*(np.log10(abs(array_factor2)))

    except ValueError:
        incoming_angle2=0
        array_factor_db2=0


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
                    incoming_angle3,array_factor3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')

        elif geometrical_configuration_3.get()==2:
            if scanning_tech_3.get()==1:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')

        elif geometrical_configuration_3.get()==3:
            if scanning_tech_3.get()==1:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_symmetrical_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_symmetrical_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_symmetrical_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_symmetrical_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')

        array_factor_db3=20*(np.log10(abs(array_factor3)))

    except ValueError:
        incoming_angle3=0
        array_factor_db3=0

# Create the plot.
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


def make_polar_plot(event=None):
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
                    incoming_angle,array_factor=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')

        elif geometrical_configuration_.get()==2:
            if scanning_tech_.get()==1:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_asym_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_asym_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')


        elif geometrical_configuration_.get()==3:
            if scanning_tech_.get()==1:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_symmetrical_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_symmetrical_phasescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')
            elif scanning_tech_.get()==2:
                if plane_.get()==1:
                    incoming_angle,array_factor=af_symmetrical_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'E')
                elif plane_.get()==2:
                    incoming_angle,array_factor=af_symmetrical_timescannig(b_x,b_y,b_z,f_,f0_,steering_angle_,Nx_,Ny_,Nz_,increase_rate_,'H')

        incoming_angle_radian=incoming_angle*pi/180
        array_factor=array_factor

    except ValueError:
        incoming_angle_radian=0
        array_factor=0

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
                    incoming_angle2,array_factor2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')

        elif geometrical_configuration_2.get()==2:
            if scanning_tech_2.get()==1:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_asym_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_asym_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')


        elif geometrical_configuration_2.get()==3:
            if scanning_tech_2.get()==1:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_symmetrical_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_symmetrical_phasescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')
            elif scanning_tech_2.get()==2:
                if plane_2.get()==1:
                    incoming_angle2,array_factor2=af_symmetrical_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'E')
                elif plane_2.get()==2:
                    incoming_angle2,array_factor2=af_symmetrical_timescannig(b__x,b__y,b__z,f__,f0__,steering_angle__,Nx__,Ny__,Nz__,increase_rate__,'H')

        incoming_angle_radian2=incoming_angle2*pi/180
        array_factor2=array_factor2

    except ValueError:
        incoming_angle_radian2=0
        array_factor2=0

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
                    incoming_angle3,array_factor3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')

        elif geometrical_configuration_3.get()==2:
            if scanning_tech_3.get()==1:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_asym_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_asym_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')

        elif geometrical_configuration_3.get()==3:
            if scanning_tech_3.get()==1:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_symmetrical_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_symmetrical_phasescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')
            elif scanning_tech_3.get()==2:
                if plane_3.get()==1:
                    incoming_angle3,array_factor3=af_symmetrical_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'E')
                elif plane_3.get()==2:
                    incoming_angle3,array_factor3=af_symmetrical_timescannig(b___x,b___y,b___z,f___,f0___,steering_angle___,Nx___,Ny___,Nz___,increase_rate___,'H')


        incoming_angle_radian3=incoming_angle3*pi/180
        array_factor3=array_factor3

    except ValueError:
        incoming_angle_radian3=0
        array_factor3=0

    plt.figure()
    plt.polar(incoming_angle_radian,array_factor,c='blue',label='Design 1')
    plt.polar(incoming_angle_radian2,array_factor2,c='red',label='Design 2')
    plt.polar(incoming_angle_radian3,array_factor3,c='green',label='Design 3')
    plt.legend()
    plt.show()


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


def delete_values():
    global bx,by,bz,f,f0,steering_angle,phi0,Nx,Ny,Nz,increaserate,plane_,scanning_tech_,geometrical_configuration_,b_2_x,b_2_y,b_2_z,f_2,f0_2,steering_angle_2,phi0_2,Nx_2,Ny_2,Nz_2,increaserate_2,plane_2,scanning_tech_2,geometrical_configuration_2,b_3_x,b_3_y,b_3_z,f_3,f0_3,steering_angle_3,phi0_3,Nx_3,Ny_3,Nz_3,increaserate_3,plane_3,scanning_tech_3,geometrical_configuration_3

    for i in bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increaserate,plane_,scanning_tech_,geometrical_configuration_,b_2_x,b_2_y,b_2_z,f_2,f0_2,steering_angle_2,Nx_2,Ny_2,Nz_2,increaserate_2,plane_2,scanning_tech_2,geometrical_configuration_2,b_3_x,b_3_y,b_3_z,f_3,f0_3,steering_angle_3,Nx_3,Ny_3,Nz_3,increaserate_3,plane_3,scanning_tech_3,geometrical_configuration_3:
        i.set('')


#%% Add buttons to the window:
#Cartesian Plot:
Cartesian_plot = tk.Button(window, command=make_cartesian_plot, text="Create Cartesian Plot",font=('Calibri', 11,'bold'),bg= 'dimgrey', relief=tk.RAISED, borderwidth=4).place(x=x_location+50, y=y_location+250)

#Polar Plot Button:
Polar_plot = tk.Button(window, command=make_polar_plot, text="Create Polar Plot",font=('Calibri', 11,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'dimgrey').place(x=x_location+250, y=y_location+250)

#Fill buttons:
Default_values_first_design = tk.Button(window, command=default_values_first_design, text="Fill Design 1 with default values",font=('Calibri', 10,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'linen').place(x=x_location+450, y=150)
Default_values_all_designs = tk.Button(window, command=default_values_other_designs, text="Fill Design 2&3 with default values",font=('Calibri', 10,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'linen').place(x=x_location+450, y=200)

#Clean buttons:
Delete_all_values = tk.Button(window, command=delete_values, text="Clean values",font=('Calibri', 10,'bold'),relief=tk.RAISED, borderwidth=4,bg= 'linen').place(x=x_location+450, y=250)


#To activate the window (user interface).
window.mainloop()

