# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:54:28 2023

@author: Faraj001
"""

from paraview.simple import *

def paraview_prob(bed_distance):
    
    prob_0_x=-3
    prob_0_y=-8.99
    prob_0_z=150       #50
    
    prob_1_x=44
    prob_1_y=-6.16
    prob_1_z=150      #50
    
    prob_2_x=60        #61.5   #62     #61
    prob_2_y=0.44      #1.51   #2.05   #0.97
    prob_2_z=150      #50
    
    prob_3_x=71
    prob_3_y=7.98
    prob_3_z=150      #50
    
    
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'OpenFOAMReader'
    #resultfoam = OpenFOAMReader(registrationName='result.foam', FileName='/home/saeb/OpenFoam/HPC-velocity/Wind_cyclic_12March2023/run_angle10/result.foam')
    resultfoam = OpenFOAMReader(registrationName='result.foam', FileName='./result.foam')
    ##resultfoam.MeshRegions = ['internalMesh']
    resultfoam.CellArrays = ['U', 'k', 'nut', 'omega', 'p']

    # get animation scene
    ##animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    ##animationScene1.UpdateAnimationUsingDataTimeSteps()

    # get active view
    ##renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    ##resultfoamDisplay = Show(resultfoam, renderView1, 'UnstructuredGridRepresentation')

    # get color transfer function/color map for 'p'
    ##pLUT = GetColorTransferFunction('p')

    # get opacity transfer function/opacity map for 'p'
    ##pPWF = GetOpacityTransferFunction('p')

    """
    # trace defaults for the display properties.
    resultfoamDisplay.Representation = 'Surface'
    resultfoamDisplay.ColorArrayName = ['POINTS', 'p']
    resultfoamDisplay.LookupTable = pLUT
    resultfoamDisplay.SelectTCoordArray = 'None'
    resultfoamDisplay.SelectNormalArray = 'None'
    resultfoamDisplay.SelectTangentArray = 'None'
    resultfoamDisplay.OSPRayScaleArray = 'p'
    resultfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    resultfoamDisplay.SelectOrientationVectors = 'U'
    resultfoamDisplay.ScaleFactor = 32.2
    resultfoamDisplay.SelectScaleArray = 'p'
    resultfoamDisplay.GlyphType = 'Arrow'
    resultfoamDisplay.GlyphTableIndexArray = 'p'
    resultfoamDisplay.GaussianRadius = 1.61
    resultfoamDisplay.SetScaleArray = ['POINTS', 'p']
    resultfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    resultfoamDisplay.OpacityArray = ['POINTS', 'p']
    resultfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    resultfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
    resultfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
    resultfoamDisplay.ScalarOpacityFunction = pPWF
    resultfoamDisplay.ScalarOpacityUnitDistance = 3.1570310455410118
    resultfoamDisplay.OpacityArrayName = ['POINTS', 'p']
    #resultfoamDisplay.SelectInputVectors = ['POINTS', 'U']
    resultfoamDisplay.WriteLog = ''
    """
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    ##resultfoamDisplay.ScaleTransferFunction.Points = [-545.324462890625, 0.0, 0.5, 0.0, 434.61224365234375, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    ##resultfoamDisplay.OpacityTransferFunction.Points = [-545.324462890625, 0.0, 0.5, 0.0, 434.61224365234375, 1.0, 0.5, 0.0]

    # reset view to fit data
    ##renderView1.ResetCamera(False)

    # show color bar/color legend
    ##resultfoamDisplay.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    ##renderView1.Update()

    ##animationScene1.GoToLast()

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    ##pLUT.ApplyPreset('Turbo', True)

    # set scalar coloring
    ##ColorBy(resultfoamDisplay, ('POINTS', 'U', 'Magnitude'))

    # Hide the scalar bar for this color map if no visible data is colored by it.
    ##HideScalarBarIfNotNeeded(pLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    ##resultfoamDisplay.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    ##resultfoamDisplay.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'U'
    ##uLUT = GetColorTransferFunction('U')

    # get opacity transfer function/opacity map for 'U'
    ##uPWF = GetOpacityTransferFunction('U')

    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    ##uLUT.ApplyPreset('Turbo', True)

    # create a new 'Probe Location'
    # prob bottom
    probeLocation1 = ProbeLocation(registrationName='ProbeLocation1', Input=resultfoam, ProbeType='Fixed Radius Point Source')

    # init the 'Fixed Radius Point Source' selected for 'ProbeType'
    probeLocation1.ProbeType.Center = [prob_1_x,prob_1_y+bed_distance, prob_1_z]

    # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024

    # show data in view
    ###probeLocation1Display = Show(probeLocation1, spreadSheetView1, 'SpreadSheetRepresentation')

    # get layout
    ###layout1 = GetLayoutByName("Layout #1")

    # add view to a layout so it's visible in UI
    ###AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

    # Properties modified on probeLocation1Display
    ###probeLocation1Display.Assembly = ''

    # update the view to ensure updated data information
    ##renderView1.Update()

    # update the view to ensure updated data information
    ###spreadSheetView1.Update()

    # set active source
    ###SetActiveSource(resultfoam)

    # toggle 3D widget visibility (only when running from the GUI)
    ###Hide3DWidgets(proxy=probeLocation1.ProbeType)

    # create a new 'Probe Location'
    # prob mid
    probeLocation2 = ProbeLocation(registrationName='ProbeLocation2', Input=resultfoam, ProbeType='Fixed Radius Point Source')

    # init the 'Fixed Radius Point Source' selected for 'ProbeType'
    probeLocation2.ProbeType.Center = [prob_2_x,prob_2_y+bed_distance, prob_2_z]

    # show data in view
    ###probeLocation2Display = Show(probeLocation2, spreadSheetView1, 'SpreadSheetRepresentation')

    # update the view to ensure updated data information
    ###spreadSheetView1.Update()

    # Properties modified on probeLocation2Display
    ###probeLocation2Display.Assembly = ''

    # set active source
    ###SetActiveSource(resultfoam)

    # toggle 3D widget visibility (only when running from the GUI)
    ###Hide3DWidgets(proxy=probeLocation2.ProbeType)

    # create a new 'Probe Location'
    # prob up
    probeLocation3 = ProbeLocation(registrationName='ProbeLocation3', Input=resultfoam, ProbeType='Fixed Radius Point Source')

    # init the 'Fixed Radius Point Source' selected for 'ProbeType'
    probeLocation3.ProbeType.Center = [prob_3_x,prob_3_y+bed_distance, prob_3_z]
    
    
    probeLocation0 = ProbeLocation(registrationName='ProbeLocation0', Input=resultfoam, ProbeType='Fixed Radius Point Source')

    # init the 'Fixed Radius Point Source' selected for 'ProbeType'
    probeLocation0.ProbeType.Center = [prob_0_x,prob_0_y+bed_distance, prob_0_z]

    # show data in view
    ###probeLocation3Display = Show(probeLocation3, spreadSheetView1, 'SpreadSheetRepresentation')

    # update the view to ensure updated data information
    ###spreadSheetView1.Update()

    # Properties modified on probeLocation3Display
    ###probeLocation3Display.Assembly = ''

    # set active source
    ###SetActiveSource(probeLocation2)

    # toggle 3D widget visibility (only when running from the GUI)
    ###Hide3DWidgets(proxy=probeLocation3.ProbeType)

    # set active source
    ###SetActiveSource(probeLocation1)

    # set active source
    ###SetActiveSource(probeLocation2)

    # set active source
    ###SetActiveSource(probeLocation3)

    # set active source
    ###SetActiveSource(probeLocation1)

    # set active source
    ###SetActiveSource(probeLocation2)

    # set active source
    ###SetActiveSource(probeLocation3)

    # set active source
    ###SetActiveSource(resultfoam)

    # set active source
    ###SetActiveSource(probeLocation1)

    # set active source
    ###SetActiveSource(probeLocation2)

    # set active source
    ###SetActiveSource(probeLocation3)

    # set active source
    ###SetActiveSource(probeLocation1)

    # set active source
    ###SetActiveSource(probeLocation2)

    # set active source
    ###SetActiveSource(probeLocation3)

    # set active source
    ###SetActiveSource(probeLocation1)

    # set active source
    ###SetActiveSource(probeLocation2)

    # set active source
    ###SetActiveSource(probeLocation3)

    # show data in view
    probeLocation1Display = Show(probeLocation1, spreadSheetView1, 'SpreadSheetRepresentation')

    # export view
    #ExportView('/home/saeb/OpenFoam/HPC-velocity/Wind_cyclic_12March2023/run_angle10/prob_bottom_1.csv', view=spreadSheetView1)
    ExportView('./prob_bottom.csv', view=spreadSheetView1)

    # show data in view
    probeLocation2Display = Show(probeLocation2, spreadSheetView1, 'SpreadSheetRepresentation')

    # export view
    #ExportView('/home/saeb/OpenFoam/HPC-velocity/Wind_cyclic_12March2023/run_angle10/prob_mid_1.csv', view=spreadSheetView1)
    ExportView('./prob_mid.csv', view=spreadSheetView1)

    # show data in view
    probeLocation3Display = Show(probeLocation3, spreadSheetView1, 'SpreadSheetRepresentation')

    # export view
    #ExportView('/home/saeb/OpenFoam/HPC-velocity/Wind_cyclic_12March2023/run_angle10/prob_up_1.csv', view=spreadSheetView1)
    ExportView('./prob_up.csv', view=spreadSheetView1)
    
    
    probeLocation3Display = Show(probeLocation0, spreadSheetView1, 'SpreadSheetRepresentation')

    # export view
    #ExportView('/home/saeb/OpenFoam/HPC-velocity/Wind_cyclic_12March2023/run_angle10/prob_up_1.csv', view=spreadSheetView1)
    ExportView('./prob_0.csv', view=spreadSheetView1)

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    ##layout1.SetSize(917, 528)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    ##renderView1.CameraPosition = [264.8207859950608, 145.4359820905942, 711.4552550546482]
    ##renderView1.CameraFocalPoint = [150.99999999999997, 39.99999999999999, 49.999999999999964]
    ##renderView1.CameraViewUp = [-0.02901509284073772, 0.9878812438491911, -0.1524754814336342]
    ##renderView1.CameraParallelScale = 175.84368058022443

    #--------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
