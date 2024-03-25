

from paraview.simple import *

import pandas as pd
import csv
import os


def get_result_prob(prob_coordinates,result_foam_directory,profile_coordinates, result_file_directory):
      
    paraview.simple._DisableFirstRenderCameraReset()
    
    directory_OpenFoam_result = f'{result_foam_directory}/result.foam'
    
    # create a new 'OpenFOAMReader'
    
    #resultfoam = OpenFOAMReader(registrationName='result.foam', FileName=result_foam_directory)
    resultfoam = OpenFOAMReader(registrationName='result.foam', FileName=directory_OpenFoam_result)

    resultfoam.CellArrays = ['U', 'k', 'nut', 'omega', 'p']

    # Create a new 'SpreadSheet View'
    spreadSheetView = CreateView('SpreadSheetView')
    spreadSheetView.ColumnToSort = ''
    spreadSheetView.BlockSize = 1024
 
 
    probe_data_dict = {}

    for probe_name, coordinates in prob_coordinates.items():
 
        prob_x, prob_y, prob_z = coordinates
    
        ## Create a new 'Probe Location'
        resultfoam.CellArrays = ['U', 'k', 'nut', 'omega', 'p']
        probeLocation = ProbeLocation(registrationName=f'probeLocation{probe_name}', Input=resultfoam, ProbeType='Fixed Radius Point Source')

        # Set the probe location coordinates
        probeLocation.ProbeType.Center = [prob_x, prob_y, prob_z]

        # Show the probe location in the SpreadSheetView
        
        probeLocationDisplay = Show(probeLocation, spreadSheetView, 'SpreadSheetRepresentation')
        
        # update the view to ensure updated data information
        spreadSheetView.Update()
        
        # Export view to CSV file
        file_name = 'CSV_results_directory.csv'
        ExportView(file_name, view=spreadSheetView)
          
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
        
        # Write the probe data to CSV file
    with open(result_file_directory, 'w', newline='') as file:
        write_file = csv.writer(file)

        # Check if result_file.csv exists or is empty
        write_header = not (os.path.exists(result_file_directory) and os.path.getsize(result_file_directory) > 0)

        if write_header:
            header_row = ['x', 'y', 'U_magnitude', 'U_x', 'U_y', 'U_z']
            write_file.writerow(header_row)

        for i, probe_name in enumerate(probe_data_dict.keys()):
            probe_data = probe_data_dict[probe_name]
            # Extract the data row
            if probe_data['U_magnitude'][0] != 0:
                data_row = [profile_coordinates[i][0]] + [profile_coordinates[i][1]] + [probe_data[key][0] for key in ['U_magnitude', 'U_x', 'U_y', 'U_z']]
                write_file.writerow(data_row)
