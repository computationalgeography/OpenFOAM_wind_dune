import numpy as np


def set_coordinate(input_2D_data_file, output_3D_data_file, Z_initial_coordinate, Z_depth, Z_delta_space):
    data = np.loadtxt(input_2D_data_file)
    Z_num = np.fix(Z_depth / Z_delta_space) + 1
    data_3D = np.zeros((int(Z_num) * data.shape[0], 3))
    for z_index in range(int(Z_num)):
        delta_Z_space = (Z_depth / (Z_num - 1))
        Z_coordinate = Z_initial_coordinate + ((z_index) * delta_Z_space)
        for i in range(data.shape[0]):
            x = data[i, 0]
            y = data[i, 1]
            data_3D[(z_index * data.shape[0]) + i, 0] = x
            data_3D[(z_index * data.shape[0]) + i, 1] = y
            data_3D[(z_index * data.shape[0]) + i, 2] = Z_coordinate
            
            
    file_name = output_3D_data_file
    np.savetxt(file_name, data_3D)
    #return data_3D

