#!/bin/sh


for angle_parameter in 89      # 80 90 #70  #0 10 20 30 40 45 50 60   #70 80 90 # 0 10 20 30 # 50    # 40 45 50 60 # 30    #4 1 2 

do

mkdir run_angle$angle_parameter

#cp -r {0,system,constant,Allclean,Allrun,plot_gnuplot_residuals}  run_Mesh_factor$Mesh_refined_factor_parameter
cp -r {0,system,constant,Allrun}  run_angle$angle_parameter

cd run_angle$angle_parameter

#foamDictionary -entry Mesh_refined_factor\  -set  2  system/blockMeshDict

#foamDictionary -entry "Mesh_refined_factor"\  -set  "5"  system/blockMeshDict  // inha chon comment haye dahele file ra hazf mikard azash estefade nakardam vagarne be nazar dorost kar mikard.

#The below command should be keep in this line (line 38) otherwise the sed does not work correct.
#sed -i "38s/.*/Mesh_refined_factor    $Mesh_refined_factor_parameter ;/" system/blockMeshDict 
sed -i "48s/.*/teta_wind_velocity_degree   $angle_parameter ;/" 0/include/initialConditions 


#bash Allclean_bash.sh    #./Allclean

#nohup sh Allclean_bash.sh  > nohup_Allclean_bash.out &

#bash Allrun_bash.sh      #./Allrun

#nohup sh Allrun_bash.sh  > Allrun_bash.out &

#nohup sh Allrun_bash.sh &

./Allrun


#bash plot_gnuplot_residuals.sh    #./plot_gnuplot_residuals

#nohup sh plot_gnuplot_residuals.sh &

#nohup sh plot_gnuplot_residuals.sh  > plot_gnuplot_residuals.out &

# mv residual.pdf residual$Mesh_refined_factor_parameter.pdf

#mv logs logs$Mesh_refined_factor_parameter   # in error midad chon dakhele plot_gnuplot_residuals.sh  logs.U_x call mikonad baraye plot

cd ..

done
