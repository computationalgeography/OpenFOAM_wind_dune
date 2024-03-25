

import set_data_2D_ideal_profile
import set_3D_coordinate_profile

import update_OpenFoam_file

import stl_3D_profile

import os

import sys

# Check if the data file name is provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide the data file name as a command line argument.")
    sys.exit(1)

data_file_name = sys.argv[1]



#--------------------------------------------read the data file and generate the profile coordinateds and parameters-----------------------------------------------------

# Initialize variables

x_0=None  # The intial location for geometry to avoid from the erro of "FOAM FATAL ERROR: bad set size ..." 
y_0=None  # The intial location for geometry to avoid from the erro of "FOAM FATAL ERROR: bad set size ..."

#y_end_domain= None
z_0_domain = None
z_end_domain = None

#H1=None
H2=None
H3=None
H4=None

l1=None
l4=None
l6=None

s1=None
s2=None
s3=None

initial_mesh_number_each_direction=None

with open(data_file_name, 'r') as file:
    # Read the lines from the file
    lines = file.readlines()

# Process the lines
for line in lines:
    
    
    # Skip lines starting with //
    if line.startswith('//'):
        continue
    
    # Remove comments from the line
    if '//' in line:
        line = line[:line.index('//')]
        
    parts_info = line.strip().split()
        
    # Skip lines without a key and value
    if len(parts_info) != 2:
        continue
        
    # Split the line into key and value
    key, value = parts_info

    # Assign the values to variables
    if key == 'x_0':    
       try:
           x_0 = float(value)
       except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")                     
    elif key == 'y_0':
        try:
           y_0 = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    #elif key == 'y_end':
    #    try:
    #       y_end_domain = float(value)
    #    except ValueError:   
    #       print(f"Error converting value to float for key '{key}': {value}")
    elif key == 'z_0':       
        try:
           z_0_domain = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    elif key == 'z_end':
        try:
           z_end_domain = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    #elif key == 'H1':
    #    try:
    #       H1 = float(value)
    #    except ValueError:   
    #       print(f"Error converting value to float for key '{key}': {value}")
    elif key == 'H2': 
        try:
           H2 = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    elif key == 'H3':
        try:
           H3 = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    elif key == 'H4':
        try:
           H4 = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    elif key == 'l1':
        try:
           l1 = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    elif key == 'l4':
        try:
           l4 = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    elif key == 'l6':
        try:
           l6 = float(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")
    elif key == 's1':
        try:
            s1 = float(eval(value))
        except (SyntaxError, ZeroDivisionError):
            print(f"Error evaluating expression for key '{key}': {value}")
    elif key == 's2':
        try:
            s2 = float(eval(value))
        except (SyntaxError, ZeroDivisionError):
            print(f"Error evaluating expression for key '{key}': {value}")
    elif key == 's3':
        try:
            s3 = float(eval(value))
        except (SyntaxError, ZeroDivisionError):
            print(f"Error evaluating expression for key '{key}': {value}")
    elif key == 'initial_mesh_number_each_direction':
        try:
            initial_mesh_number_each_direction = int(value)
        except ValueError:   
           print(f"Error converting value to float for key '{key}': {value}")        
            
      

#-------------------------------------------- generate the profile coordinateds and parameters----------------------------------------------

if not os.path.exists('profile_coordinates'):
    os.makedirs('profile_coordinates')

output_2D_profile_coordinate = 'profile_coordinates/Ideal_profile_2D.txt'
output_file_info_geometry = 'info_2D_profile.txt'

set_data_2D_ideal_profile.set_data(output_2D_profile_coordinate,output_file_info_geometry,x_0, y_0, z_0_domain, z_end_domain, H2, H3, H4, l1, l4, l6, s1, s2, s3,initial_mesh_number_each_direction)


#-------------------------------------------- End: Generate the profile coordinateds and parameters----------------------------------------------

#-------------------------------------------- Revise the openfoam 'initialConditions' file---------------------------------------------------
input_file = output_file_info_geometry
output_file = 'OpenFoam_file/initialConditions'       # This is OpenFoam file that should be edited. esme file vorodi OpenFoam hast ke parametrhash bayad eslah shavad


keyword_list = ['x_v0_domain', 'y_v0_domain', 'x_v1_domain', 'y_v1_domain', 'y_end_domain',
                'z_0_domain', 'z_end_domain', 'x_front_beach', 'x_front_fordune',
                'x_top', 'x_back']

update_OpenFoam_file.update_file(input_file, output_file, keyword_list)



input_file_snappyHexMeshDict = output_file_info_geometry
output_file_snappyHexMeshDict = 'OpenFoam_file/snappyHexMeshDict'       # This is OpenFoam file that should be edited. esme file vorodi OpenFoam hast ke parametrhash bayad eslah shavad

keyword_list_snappyHexMeshDict = ['insidePoint']

update_OpenFoam_file.update_file(input_file_snappyHexMeshDict, output_file_snappyHexMeshDict, keyword_list_snappyHexMeshDict)


input_file = output_file_info_geometry
output_file = 'OpenFoam_file/blockMeshDict'       # This is OpenFoam file that should be edited. esme file vorodi OpenFoam hast ke parametrhash bayad eslah shavad


keyword_list_mesh_num = ['num_mesh_split_x', 'num_mesh_split_y', 'num_mesh_split_z']

update_OpenFoam_file.update_file(input_file, output_file, keyword_list_mesh_num)



#-------------------------------------------- End: Revise the openfoam 'initialConditions' file---------------------------------------------------

#-------------------------------------------- creade 3D coordinate data from 2D_coordinate data file ---------------------------------------------

input_2D_data_file =output_2D_profile_coordinate  #data_refined_2D
output_3D_data_file = 'profile_coordinates/Ideal_profile_3D.txt'

Z_initial_coordinate = z_0_domain
Z_depth = z_end_domain
Z_delta_space = 1

set_3D_coordinate_profile.set_coordinate(input_2D_data_file,output_3D_data_file,Z_initial_coordinate,Z_depth,Z_delta_space)

#-------------------------------------------- End: Creade 3D coordinate data from 2D_coordinate data file ---------------------------------------------

#--------------------------------------------------------- Create stl file for bed profile geometry ---------------------------------------------------

if not os.path.exists('stl'):
    os.makedirs('stl')
    
input_3D_coordinate_file = output_3D_data_file
output_stl_file = 'stl/ground'

x_0 = x_0
z_0 = z_0_domain
Z_depth = z_end_domain


#********* Read value x_end ************

with open(output_file_info_geometry, 'r') as file:
    for line in file:
        if line.startswith("x_v1_domain"):
            x_end = float(line.split()[1])
            break  # Stop searching after finding the line
            
#********* End: Read value x_end *******


stl_3D_profile.stl_3D(input_3D_coordinate_file,output_stl_file,x_0,x_end,z_0,Z_depth)

#--------------------------------------------------------- End: Create stl file for bed profile geometry -----------------------------------------------
