#!/bin/sh

#H3_values=(6 9 12 15 18 24 25)
#s1_values=(0.01 0.05 0.1)
#s2_values=(0.33 0.25 0.5 1)

H3_values=(25)   #(6 9 12 15 18 24 25)
s1_values=(0.1)  #(0.01 0.05 0.1)
s2_values=(0.33)
angle_parameter=(0 10 80)
#angle_parameter_708090=(70 80 89)
bed_distance=0.5


for H3 in "${H3_values[@]}"; do
    for s1 in "${s1_values[@]}"; do
        for s2 in "${s2_values[@]}"; do
		       for angle in "${angle_parameter[@]}"; do 

				   sed -i "s/H3 .*/H3 ${H3}/; s/s1 .*/s1 ${s1}/; s/s2 .*/s2 ${s2}/; s/angle .*/angle ${angle}/" "data_file.txt"
				   
                   sed -i "s/H3 .*/H3 ${H3}/; s/s1 .*/s1 ${s1}/; s/s2 .*/s2 ${s2}/; s/angle .*/angle ${angle}/" "data_file_708090.txt" 

				   export RESULT_FOAM_DIRECTORY=../H3_${H3}_s1_${s1}_s2_${s2}/run_angle${angle}
				   
				   export eMesh_bed_file_FOAM_DIRECTORY=../H3_${H3}_s1_${s1}_s2_${s2}/constant/geometry/ground.eMesh
				   
				   file_name=H3_${H3}_s1_${s1}_s2_${s2}/run_angle${angle}

                   echo "$file_name"
				   
				   if [ $angle -gt 60 ]; then 
				   
				   export data_profile_file=data_file_708090.txt

                   else 
				   
				   export data_profile_file=data_file.txt
                   
                   fi				   
				   
				   python3 main.py $bed_distance $data_profile_file $RESULT_FOAM_DIRECTORY ratio_output.csv direction_output.csv $RESULT_FOAM_DIRECTORY $eMesh_bed_file_FOAM_DIRECTORY 				
				
			  done
				
		done
	done
done

