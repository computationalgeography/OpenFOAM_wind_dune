
import numpy as np
from scipy.interpolate import griddata
import surf2stl


def stl_3D(input_3D_coordinate_file,output_stl_file,x_0,x_end,z_0,Z_depth):
    
    data = np.loadtxt(input_3D_coordinate_file)
    
    x=data[:,0]
    y=data[:,1]
    z=data[:,2]
    x_1_grid=np.linspace(x_0, x_end, 200)
    z_1_grid=np.linspace(0, Z_depth, 200)
    xi,zi = np.meshgrid(x_1_grid,z_1_grid)
    yi = griddata((x,z),y,(xi,zi),method='linear')
    file_name =output_stl_file + ".stl"
    surf2stl.write(file_name, xi, yi, zi)







