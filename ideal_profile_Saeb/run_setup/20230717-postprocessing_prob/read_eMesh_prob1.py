import re
import numpy as np

def find_nearest_point(target_prob, file_input, bed_distance):
    # Read the eMesh file
    with open(file_input, 'r') as file:
        content = file.read()

    # Extract the coordinates using regular expressions
    pattern = r'\((-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\)'
    matches = re.findall(pattern, content)

    # Convert the coordinates to floats
    coords = np.array([[float(x), float(y), float(z)] for x, y, z in matches])

    # Initialize a dictionary to store the nearest y-coordinates
    nearest_prob_dict = {}

    # Loop through the target_prob dictionary
    for key, target in target_prob.items():
        # Extract the target x-coordinate
        target_x_value = target[0]
        

        # Calculate the distances from the target coordinate to each points
        distances = np.abs(coords[:, 0] - target_x_value)

        # Find the index of the nearest point
        nearest_index = np.argmin(distances)

        # Extract the y-coordinate of the nearest point
        nearest_y = coords[nearest_index, 1]
        nearest_x = coords[nearest_index, 0]
        

        # Update the nearest_prob_dict with the key-value pair
        if key == 'prob_1':
            nearest_prob_dict[key] = (nearest_x, nearest_y + bed_distance, target[2])
        else:
            nearest_prob_dict[key] = (target[0], target[1], target[2])

    return nearest_prob_dict
