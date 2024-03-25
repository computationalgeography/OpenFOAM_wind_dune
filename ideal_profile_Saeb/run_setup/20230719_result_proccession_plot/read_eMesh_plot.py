import re
import numpy as np

def find_nearest_point(file_input, bed_distance):
    # Read the eMesh file
    with open(file_input, 'r') as file:
        content = file.read()

    # Extract the coordinates using regular expressions
    pattern = r'\((-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\)'
    matches = re.findall(pattern, content)

    # Convert the coordinates to floats
    coords = np.array([[float(x), float(y), float(z)] for x, y, z in matches])
    
    x_0 = min(coords[:, 0])
    x_length = max(coords[:, 0])
    
    Z_center = (min(coords[:, 2])+ max(coords[:, 2]))/2
    
    num_splits=100
    target_x_prob = np.linspace(x_0, x_length, num_splits)
    
    # Initialize a dictionary to store the nearest y-coordinates
    nearest_prob_dict = {}
    profile_coordinates = [(0, 0, 0)] * len(target_x_prob)

    # Loop through the target_prob dictionary
    for i, target in enumerate(target_x_prob):
        # Extract the target x-coordinate
        
        # Calculate the distances from the target coordinate to each points
        distances = np.abs(coords[:, 0] - target)

        # Find the index of the nearest point
        nearest_index = np.argmin(distances)

        # Extract the y-coordinate of the nearest point
        nearest_y = coords[nearest_index, 1]
        nearest_x = coords[nearest_index, 0]
        

        # Update the nearest_prob_dict with the key-value pair
        key = f'prob_{i}'
        nearest_prob_dict[key] = (nearest_x, nearest_y+bed_distance, Z_center)
        profile_coordinates [i] = (nearest_x, nearest_y, Z_center)

    return nearest_prob_dict, profile_coordinates
