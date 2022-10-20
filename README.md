WORKING WITH THE SIMULATOR (USER INTERFACE):

The main script which needs to be executed is 'arrayfactortool.py' to open the User Interface. Firstly, please pay attention to the working directory.

NOTE 1: Before executing the tool, please pay attention to the requirements.txt which gives the required libraries that must be installed:

tkinter
os
PIL==6.1.0
scipy==1.2.1
cmath
numpy==1.16.4
matplotlib==3.1.0

NOTE 2: This interface was created by Spyder 3.3.6  and Python 3.7.3.
NOTE 3: If the script gives an error about Images (i.e. TclError) please restart kernel
NOTE 4: In order to observe the theory behind this tool, please check Theory of Array Factor.pdf.

The rest of the scripts, which contain main equations given in Theory of Array Factor.pdf, are briefly explained below:
These scripts are stored in 'array_factor_equations'.

arrayfactor_asym_phasescanning.py: Array factor calculation with Phase Shifting method for asymmetrically configured array.
arrayfactor_asym_timescanning.py:  Array factor calculation with True Time Delay method for asymmetrically configured array.
arrayfactor_symmetrical_phasescanning.py: Array factor calculation with Phase Shifting method for symmetrically configured array.
arrayfactor_symmetrical_timescanning.py: Array factor calculation with True Time Delay method for symmetrically configured array.


All of these scripts must be placed in the same folder which must be working directory of 'arrayfactortool.py'. 
Besides them, images folder which includes figures used in the interface is also required to be in the same folder with those.


The results of the user interface are consistent with the results already published in the literature which can be found in references folder.

#################################################################################################################################################################

WORKING WITHOUT THE SIMULATOR (USER INTERFACE):

It is also possible to obtain the results/plots only using the scripts individually which are stored in 'array_factor_equations' folder.
They contain the relevant equations used to calculate AF patterns.
