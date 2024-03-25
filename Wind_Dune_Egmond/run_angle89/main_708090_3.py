
#from paraview.simple import *


import function_paraview_708090_3
import function_U_ratio_calculate_3

Bed_Distance=0.5   #1  

Bed_Distance_prob0=10  

function_paraview_708090_3.paraview_prob(Bed_Distance,Bed_Distance_prob0)

function_U_ratio_calculate_3.U_ratio_calculate(Bed_Distance,Bed_Distance_prob0)
