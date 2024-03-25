#!/bin/sh

H3_values=(6 9 12 15 18 21 25)
s1_values=(0.01 0.05 0.1)
#s2_values=(0.25 0.33 0.5 1)
s2_values=(1)


#H3_values=(9)
#s1_values=(0.01)
#s2_values=(0.25 0.33 0.5 1)

#-----------------------------------create required stl and initialConditions file -----------------------------------------

cd created_info_profile 

for H3 in "${H3_values[@]}"; do
    for s1 in "${s1_values[@]}"; do
        for s2 in "${s2_values[@]}"; do
		       
                mkdir H3_${H3}_s1_${s1}_s2_${s2}

                cp -r ../goemetry_setup/{main_ideal_profile.py,set_3D_coordinate_profile.py,set_data_2D_ideal_profile.py,stl_3D_profile.py,update_OpenFoam_file.py,OpenFoam_file,profile_geometry}  H3_${H3}_s1_${s1}_s2_${s2}

                cd H3_${H3}_s1_${s1}_s2_${s2}
				
				sed -i "s/H3 .*/H3 ${H3}/; s/s1 .*/s1 ${s1}/; s/s2 .*/s2 ${s2}/" "profile_geometry/data_file.txt" 
				
				python3 main_ideal_profile.py profile_geometry/data_file.txt
				
				cd ..
				
		done
	done
done

#------------------------------------------------setup OpenFoam files ---------------------------------------------------------

cd ../run_setup 

for H3 in "${H3_values[@]}"; do
    for s1 in "${s1_values[@]}"; do
        for s2 in "${s2_values[@]}"; do
		       
                mkdir H3_${H3}_s1_${s1}_s2_${s2}

                cp -r ../OpenFoam_setup/*  H3_${H3}_s1_${s1}_s2_${s2}
				
				cp  ../created_info_profile/H3_${H3}_s1_${s1}_s2_${s2}/stl/*  H3_${H3}_s1_${s1}_s2_${s2}/constant/geometry
				
				cp  ../created_info_profile/H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_file/initialConditions  H3_${H3}_s1_${s1}_s2_${s2}/0/include
				
				cp  ../created_info_profile/H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_file/snappyHexMeshDict  H3_${H3}_s1_${s1}_s2_${s2}/system
				
				cp  ../created_info_profile/H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_file/blockMeshDict  H3_${H3}_s1_${s1}_s2_${s2}/system
				
				cd H3_${H3}_s1_${s1}_s2_${s2}
				bash snappy.sh
				cd ../

				
		done
	done
done


#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------create required stl and initialConditions file 708090-----------------------------------------

cd ../created_info_profile 

for H3 in "${H3_values[@]}"; do
    for s1 in "${s1_values[@]}"; do
        for s2 in "${s2_values[@]}"; do
		       
                mkdir H3_${H3}_s1_${s1}_s2_${s2}_708090

                cp -r ../goemetry_setup/{main_ideal_profile.py,set_3D_coordinate_profile.py,set_data_2D_ideal_profile.py,stl_3D_profile.py,update_OpenFoam_file.py,OpenFoam_file,profile_geometry}  H3_${H3}_s1_${s1}_s2_${s2}_708090
                
				cd H3_${H3}_s1_${s1}_s2_${s2}_708090
				
				sed -i "s/H3 .*/H3 ${H3}/; s/s1 .*/s1 ${s1}/; s/s2 .*/s2 ${s2}/" "profile_geometry/data_file_708090.txt" 
				
				python3 main_ideal_profile.py profile_geometry/data_file_708090.txt
				
				cd ..
				
		done
	done
done

#------------------------------------------------setup OpenFoam files 708090---------------------------------------------------------


cd ../run_setup 

for H3 in "${H3_values[@]}"; do
    for s1 in "${s1_values[@]}"; do
        for s2 in "${s2_values[@]}"; do
		       
                mkdir  H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_708090

                cp -r ../OpenFoam_setup/*  H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_708090
				
				cp  ../created_info_profile/H3_${H3}_s1_${s1}_s2_${s2}_708090/stl/*  H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_708090/constant/geometry
				
				cp  ../created_info_profile/H3_${H3}_s1_${s1}_s2_${s2}_708090/OpenFoam_file/initialConditions  H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_708090/0/include
				
				cp  ../created_info_profile/H3_${H3}_s1_${s1}_s2_${s2}_708090/OpenFoam_file/snappyHexMeshDict  H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_708090/system
				
				cp  ../created_info_profile/H3_${H3}_s1_${s1}_s2_${s2}_708090/OpenFoam_file/blockMeshDict  H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_708090/system
				
				cd H3_${H3}_s1_${s1}_s2_${s2}/OpenFoam_708090
				bash snappy.sh
				cd ../..
				
		done
	done
done


