

from paraview.simple import *

def get_result_prob(prob_coordinates,result_foam_directory,CSV_results_directory):
      
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
        file_name = f'{CSV_results_directory}/{probe_name}.csv'
        ExportView(file_name, view=spreadSheetView)
        
        
        
    

   
