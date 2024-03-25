import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import csv

def U_ratio_diraction_calculate(profile_value, num_probes, ratio_output, direction_output, CSV_results_directory):
    probe_data_dict = {}
    
    for i in range(num_probes):
        probe_name = f'prob_{i}'
        file_name = f'{CSV_results_directory}/{probe_name}.csv'
        
        data = pd.read_csv(file_name)
        
        U_magnitude = data['U_Magnitude'].values  
        U_x = data['U_0'].values  
        U_y = data['U_1'].values  
        U_z = data['U_2'].values  

        probe_data_dict[probe_name] = {
            'U_magnitude': U_magnitude,
            'U_x': U_x,
            'U_y': U_y,
            'U_z': U_z
        }
        
    with open(ratio_output, 'a', newline='') as file:
        write_file = csv.writer(file)
        
        # Check if ratio_output file exists or is empty
        write_header = not (os.path.exists(ratio_output) and os.path.getsize(ratio_output) > 0)
        
        if write_header:
            # Write the header row
            header_row = list(profile_value.keys()) + [f'velocity ratio prob {i} to prob {j}' for i in range(num_probes) for j in range(num_probes) if j != i]
            write_file.writerow(header_row)
        
        data_row = list(profile_value.values())
        
        for i in range(num_probes):
            probe_name_i = f'prob_{i}'
            
            for j in range(num_probes):
                if j != i:
                    probe_name_j = f'prob_{j}'
                    U_mag_ratio = float(probe_data_dict[probe_name_i]['U_magnitude'] / probe_data_dict[probe_name_j]['U_magnitude'])
                    data_row.append(U_mag_ratio)
            
        write_file.writerow(data_row)
    
    with open(direction_output, 'a', newline='') as file_direction:
        write_file = csv.writer(file_direction)
        
        # Check if direction_output file exists or is empty
        write_header = not (os.path.exists(direction_output) and os.path.getsize(direction_output) > 0)
        
        if write_header:
            # Write the header row
            header_row = list(profile_value.keys()) + [f'velocity direction prob {i}' for i in range(num_probes)]
            write_file.writerow(header_row)
        
        data_row = list(profile_value.values())

        for i in range(num_probes):
            probe_name_i = f'prob_{i}'
            direct_velocity = math.atan(probe_data_dict[probe_name_i]['U_z'] / probe_data_dict[probe_name_i]['U_x']) * (180 / math.pi)
            data_row.append(direct_velocity)
        
        write_file.writerow(data_row)
