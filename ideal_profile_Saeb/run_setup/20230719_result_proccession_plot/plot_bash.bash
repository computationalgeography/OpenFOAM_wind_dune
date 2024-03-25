#!/bin/sh

#H3_values=(6 9 12 15 18 24 25)
#s1_values=(0.01 0.05 0.1)
#s2_values=(0.33 0.25 0.5 1)


H3_values=(6 25)   #(6 9 12 15 18 24 25)
s1_values=(0.1)  #(0.01 0.05 0.1)
s2_values=(0.33)
angle_parameter=(0 10 80)
#angle_parameter_708090=(70 80 89)
bed_distance=1


for H3 in "${H3_values[@]}"; do
    for s1 in "${s1_values[@]}"; do
        for s2 in "${s2_values[@]}"; do
		       for angle in "${angle_parameter[@]}"; do 

				   export RESULT_FOAM_DIRECTORY=../H3_${H3}_s1_${s1}_s2_${s2}/run_angle${angle}
				   export result_excel_file=../H3_${H3}_s1_${s1}_s2_${s2}/run_angle${angle}/plot_centerline_velocity.csv
				   
				   export result_plot=./plot_all_velocity
				   
				   export eMesh_bed_file_FOAM_DIRECTORY=../H3_${H3}_s1_${s1}_s2_${s2}/constant/geometry/ground.eMesh
				   
				   file_name=H3_${H3}_s1_${s1}_s2_${s2}/run_angle${angle}

                   echo "$file_name"

				   python3 main.py $bed_distance $eMesh_bed_file_FOAM_DIRECTORY $RESULT_FOAM_DIRECTORY $result_excel_file $result_plot
				
			  done
				
		done
	done
done

