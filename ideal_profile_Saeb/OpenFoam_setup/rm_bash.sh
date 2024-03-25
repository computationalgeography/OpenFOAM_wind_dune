#!/bin/sh


for angle_parameter in 0 10 20 30 40 45 50 60 #70 80 90 #70 80 90  #0 10 20 30 40 45 50 60   #70 80 90 # 0 10 20 30 # 50 70 80   # 40 45 50 60 # 30    #4 1 2 

do



cd run_angle$angle_parameter

rm -r processor*

rm -r {100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900}

rm -r postProcessing

rm Allclean_bash.sh

rm Allrun_bash.sh

rm plot_gnuplot_residuals.sh

rm residual.pdf

rm write_L1_band

rm write_x_roughness

rm write_y_inlet_result_elevation*

rm log.*


cd ..

done
