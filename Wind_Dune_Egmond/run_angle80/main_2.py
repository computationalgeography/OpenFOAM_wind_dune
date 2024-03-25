
#from paraview.simple import *


import function_paraview_2
import function_U_ratio_calculate

Bed_Distance=0.5   #1  

function_paraview_2.paraview_prob(Bed_Distance)

function_U_ratio_calculate.U_ratio_calculate(Bed_Distance)
