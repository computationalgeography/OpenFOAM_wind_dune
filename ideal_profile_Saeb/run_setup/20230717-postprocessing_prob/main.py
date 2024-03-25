
import sys
import json

import extract_result_paraview
import result_processing
import prob_coordinate_setup

#import read_eMesh
import read_eMesh_prob1


if len(sys.argv) < 8 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(" Please enter sufficient input arguments and look at usage: python main.py <bed_distance> <data_profile> <result_OpenFoam_directory> <velocity_ratio_output_file> <velocity_direction_output_file> <CSV_results_directory>")
    print("Arguments:")
    print("  bed_distance:       value for distance of prob above bed in y direction")
    print("  data_profile:       Path to the data profile file")
    print("  result_foam_directory: Path to the result OpenFoam directory : path/to/OpenFoam/results")
    print("  velocity_ratio_output_file:  Path to the ratio output file")
    print("  velocity_direction_output_file:  Path to the direction output file")
    print("  CSV_results_directory:  Path to the directory to save CSV files extracting probs velocity results by paraview\n")
    print (" example of run: python3 main.py 0.5 data_file.txt $RESULT_FOAM_DIRECTORY ratio_output.csv direction_output.csv ../H3_6_s1_0.01_s2_0.25/run_angle0\n"
           " the diroctory  $RESULT_FOAM_DIRECTORY=../H3_6_s1_0.01_s2_0.25/run_angle0\n")
    print (" ground_eMesh_file")       
           
    sys.exit(0)

bed_distance = sys.argv[1] 
data_profile = sys.argv[2]
result_foam_directory = sys.argv[3]
ratio_output_file = sys.argv[4]
direction_output_file = sys.argv[5]
CSV_results_directory  = sys.argv[6]
ground_eMesh_file = sys.argv[7]

'''prob_coordinate_setup function take data_profile including H3,s1,s2 and so on and returns the coordinates of probs'''
prob_coordinate_dict, profile_data_dict = prob_coordinate_setup.set_coordinates(data_profile, float(bed_distance))


print('prob_coordinate_dict', prob_coordinate_dict) 

#dict_edited_prob =read_eMesh.find_nearest_point(prob_coordinate_dict, ground_eMesh_file, float(bed_distance))
dict_edited_prob =read_eMesh_prob1.find_nearest_point(prob_coordinate_dict, ground_eMesh_file, float(bed_distance))


print('dict_edited_prob', dict_edited_prob)

with open('prob_coordinates.txt', 'w') as file:
        json.dump(dict_edited_prob, file)

'''Extract the results in probs locations according to obtained OpenFoam results'''
extract_result_paraview.get_result_prob(dict_edited_prob,result_foam_directory,CSV_results_directory)

num_probes = len(dict_edited_prob)

'''Calculate the veocity ration and velocity direction in probs'''
result_processing.U_ratio_diraction_calculate(profile_data_dict, num_probes, ratio_output_file, direction_output_file, CSV_results_directory)



