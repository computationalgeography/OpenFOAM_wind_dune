
import sys
import json

import extract_result_paraview_plot

import read_eMesh_plot

import plot_results

import plot_to_docx

if len(sys.argv) < 5 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(" Please enter sufficient input arguments and look at usage: python main.py <bed_distance> <data_profile> <result_OpenFoam_directory> <velocity_ratio_output_file> <velocity_direction_output_file> <CSV_results_directory>")
    print("Arguments:")
    print("  bed_distance:       value for distance of prob above bed in y direction")
    print (" ground_eMesh_file")    
    print ("result_foam_directory ")   
    print ("result_file_directory ")   
    
    
    sys.exit(0)

bed_distance = sys.argv[1] 
ground_eMesh_file = sys.argv[2]
result_foam_directory = sys.argv[3]
result_file_directory = sys.argv[4]
plot_directory = sys.argv[5]


dict_edited_prob ,profile_coordinates =read_eMesh_plot.find_nearest_point(ground_eMesh_file, float(bed_distance))

#print('dict_edited_prob', dict_edited_prob)


'''Extract the results in probs locations according to obtained OpenFoam results'''
extract_result_paraview_plot.get_result_prob(dict_edited_prob,result_foam_directory,profile_coordinates, result_file_directory)


'''plot results'''

plot_results.plot_data(result_file_directory, 'x', 'y', 'U_magnitude', result_foam_directory, plot_directory)




