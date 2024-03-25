

import numpy as np
import matplotlib.pyplot as plt

def set_data(output_2D_profile_coordinate,output_file_info_geometry,x_0, y_0, z_0_domain, z_end_domain, H2, H3, H4, l1, l4, l6, s1, s2, s3,initial_mesh_number_each_direction):
    data = np.zeros((7, 2))
    
    # Calculate the geometry values
    l2 = H2 / s1
    l3 = (H3 - H2) / s2
    l5 = (H3 - H4) / s3
    
    l6 = max(l6, 3*H3)
    
    x1 = x_0 + l1
    y1 = y_0
    x2 = x_0 + l1 + l2
    y2 = y_0 + H2
    x3 = x_0 + l1 + l2 + l3
    y3 = y_0 + H3
    x4 = x_0 + l1 + l2 + l3 + l4
    y4 = y_0 + H3
    x5 = x_0 + l1 + l2 + l3 + l4 + l5
    y5 = y_0 + H4
    x_end = x_0 + l1 + l2 + l3 + l4 + l5 + l6
    y_end = y_0 + H4
    
    H1 = 4*H3
    
    y_end_domain = y_0+H1
    
    insidePoint_x = l1/2
    insidePoint_y = y_0+(H1/2)
    insidePoint_z = (z_0_domain+z_end_domain)/2
    
    s1_factor_x =1 
    
    if s1 < 0.01 or s1 >= 0.05:
         s1_factor_x = 2
    elif s1 >= 0.01:
        s1_factor_x = 3
    #L_factor = (l1+l2+l3+l4+l5+l6)/200
    
    #initial_delta_space = (y_end-y_0)/initial_mesh_number_each_direction  
    num_mesh_split_y = int(1 * max(initial_mesh_number_each_direction,int((s2/0.25)*0.5*H3)))   #initial_mesh_number_each_direction
    #num_mesh_split_x = int((x_end-x_0)/initial_delta_space)
    #num_mesh_split_z = int((z_end_domain-z_0_domain)/initial_delta_space)
    min_L_parts= min(l1,l2,l3,l4,l5,l6)
    num_split_min_L_parts = max(int((1/0.25)*(H3/5)/2),1)   #max(int((s2/0.25)*(H3/5)/2),1)
    
    print (f'min_L_parts {min_L_parts}  num_split_min_L_parts {num_split_min_L_parts}')
    initial_delta_space_x = min_L_parts/num_split_min_L_parts          #(l3 + l4 + l5)/(initial_mesh_number_each_direction)     #(l3 + l4 + l5)/(initial_mesh_number_each_direction/3)
    num_mesh_split_x_min_L_parts = int((x_end-x_0)/(initial_delta_space_x))
    
    num_mesh_split_x = int(s1_factor_x*max(initial_mesh_number_each_direction,num_mesh_split_x_min_L_parts,200))    #int(max((L_factor*initial_mesh_number_each_direction),num_mesh_split_x_min_L_parts))     #int((x_end-x_0)/initial_delta_space_x)
    num_mesh_split_z = int(num_mesh_split_y)
    
    print(f' num_mesh_split_x {num_mesh_split_x} num_mesh_split_y {num_mesh_split_y} num_mesh_split_z {num_mesh_split_z}')

    # Store the geometry values in the data array
    data[0, 0] = x_0
    data[0, 1] = y_0
    data[1, 0] = x1
    data[1, 1] = y1
    data[2, 0] = x2
    data[2, 1] = y2
    data[3, 0] = x3
    data[3, 1] = y3
    data[4, 0] = x4
    data[4, 1] = y4
    data[5, 0] = x5
    data[5, 1] = y5
    data[6, 0] = x_end
    data[6, 1] = y_end
    
    # Save the data to output_2D_profile_coordinate
    #np.savetxt(output_2D_profile_coordinate, data, delimiter='\t')
    
    # Write the initial conditions to Ideal_profile_2D_inof_for_initialConditions.txt
    with open(output_file_info_geometry, 'w') as file:
        file.write(f"x_v0_domain {data[0, 0]}\n")
        file.write(f"y_v0_domain {data[0, 1]}\n")
        file.write(f"x_v1_domain {data[-1, 0]}\n")
        file.write(f"y_v1_domain {data[-1, 1]}\n")
        file.write(f"y_end_domain {y_end_domain}\n")
        file.write(f"z_0_domain {z_0_domain}\n")
        file.write(f"z_end_domain {z_end_domain}\n")
        file.write(f"x_front_beach {x2}\n")
        file.write(f"x_front_fordune {x3}\n")
        file.write(f"x_top {x4}\n")
        file.write(f"x_back {x5}\n")
        file.write(f"insidePoint ({insidePoint_x} {insidePoint_y} {insidePoint_z})\n")
        file.write(f"num_mesh_split_x {num_mesh_split_x}\n")
        file.write(f"num_mesh_split_y {num_mesh_split_y}\n")
        file.write(f"num_mesh_split_z {num_mesh_split_z}\n")
        
    np.savetxt(output_2D_profile_coordinate, data, delimiter='\t')

    
    # in gesmat lazem nashod 
    '''data_refined_2D = [[0.0, 0.0] for _ in range(70)]


    for i in range(1, 11):  # Changed the range to include 10
        x_length = (i * (l1 / 10))
        data_refined_2D[i - 1][0] = x_0 + x_length  # Assign to the i-th row of the array   ---> in khalat ast bayad ata_refined_2D[i - 1][0] = x_0 bashad
        data_refined_2D[i - 1][1] = y_0             # Assign to the i-th row of the array
    
    for i in range(1, 11):  # Changed the range to include 10
        x_length =  (i * (l2 / 10))
        data_refined_2D[i + 9][0] = x_0 +l1 + x_length           # Assign to the i-th row of the array
        data_refined_2D[i + 9][1] = y_0 + (s1 * x_length)        # Assign to the i-th row of the array
    
    for i in range(1, 21):  # Changed the range to include 10
        x_length =  (i * (l3 / 20))
        data_refined_2D[i +19][0] = x_0 +l1 +l2+ x_length             # Assign to the i-th row of the array
        data_refined_2D[i +19][1] = y_0 + H2 + (s2 * x_length)        # Assign to the i-th row of the array
        
    for i in range(1, 11):  # Changed the range to include 10
        x_length =  (i * (l4 / 10))
        data_refined_2D[i +39][0] = x_0 +l1 +l2 + l3 + x_length  # Assign to the i-th row of the array
        data_refined_2D[i +39][1] = y_0 + H3                     # Assign to the i-th row of the array
    
    for i in range(1, 11):  # Changed the range to include 10
        x_length =  (i * (l5 / 10))
        data_refined_2D[i +49][0] = x_0 +l1 +l2+ l3 + l4 + x_length   # Assign to the i-th row of the array
        data_refined_2D[i +49][1] = y_0 + H3 - (s3 * x_length)        # Assign to the i-th row of the array
        
    for i in range(1, 11):  # Changed the range to include 10
        x_length =  (i * (l6 / 10))
        data_refined_2D[i +59][0] = x_0 +l1 +l2+ l3 + l4 + l5 + x_length   # Assign to the i-th row of the array
        data_refined_2D[i +59][1] = y_0 + H4        # Assign to the i-th row of the array
    
    
    np.savetxt(output_2D_profile_coordinate_refined, data_refined_2D, delimiter='\t')'''
    


# ![image.png](attachment:image.png)


'''
x_0=-10  # The intial location for geometry to avoid from the erro of "FOAM FATAL ERROR: bad set size ..." 
y_0=-10  # The intial location for geometry to avoid from the erro of "FOAM FATAL ERROR: bad set size ..."

y_end_domain= 100
z_0_domain = 0
z_end_domain = 100

#----------------------------------------------------------------------------------

H1=100
H2=3
H3=25
H4=5

l1=20
l4=20
l6=50

s1=1/50
s2=1/1
s3=1/3




set_data_2D_ideal_profile(output_2D_profile_coordinate,output_file_info_geometry,x_0, y_0, y_end_domain, z_0_domain, z_end_domain, H1, H2, H3, H4, l1, l4, l6, s1, s2, s3)
'''





