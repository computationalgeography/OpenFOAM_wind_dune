#!/bin/sh


for angle_parameter in 0 10 #20 30 40 45 50 60   #70 80 90 # 0 10 20 30 # 50 70 80   # 40 45 50 60 # 30    #4 1 2 

do

mkdir run_angle$angle_parameter

#cp -r {0,system,constant,Allclean,Allrun,plot_gnuplot_residuals}  run_Mesh_factor$Mesh_refined_factor_parameter
cp -r {0,system,constant,Allrun_bash.sh}  run_angle$angle_parameter

cd run_angle$angle_parameter

sed -i "s/^teta_wind_velocity_degree .*/teta_wind_velocity_degree $angle_parameter;/" 0/include/initialConditions

bash Allrun_bash.sh

wait


cd ..

done


for angle_parameter in  80 #70 89  

do

mkdir run_angle$angle_parameter

cp -r OpenFoam_708090/{0,system,constant,Allrun_bash.sh}  run_angle$angle_parameter

cd run_angle$angle_parameter

sed -i "s/^teta_wind_velocity_degree .*/teta_wind_velocity_degree $angle_parameter;/" 0/include/initialConditions

bash Allrun_bash.sh

wait

cd ..

done

