

def set_coordinates(data_file_name, bed_distance):

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
            elif key == 'angle':
                try:
                    angle = float(value)
                except ValueError:
                    print(f"Error converting value to float for key '{key}': {value}")
                    
    l2=H2/s1
    l3=(H3-H2)/s2
    
    prob_coordinate_dict = {}
    
    prob_coordinate_dict['prob_0'] = (x_0 + l1 + (l2 / 2), y_0 + (H2/ 2) + bed_distance, (z_0_domain + z_end_domain) / 2)
        
    prob_coordinate_dict['prob_1'] = (x_0 + l1 + l2 , y_0 + H2 + bed_distance, (z_0_domain + z_end_domain) / 2)
        
    prob_coordinate_dict['prob_2'] = (x_0 + l1 + l2 +(l3 / 2), y_0 + ((H2+H3)/ 2) + bed_distance, (z_0_domain + z_end_domain) / 2)
        
    prob_coordinate_dict['prob_3'] = (x_0 + l1 + l2 + l3 , y_0 + H3 + bed_distance, (z_0_domain + z_end_domain) / 2)
    
    profile_data_dict = {}
    profile_data_dict['H3'] = H3
    profile_data_dict['s1'] = s1
    profile_data_dict['s2'] = s2
    profile_data_dict['angle'] = angle
  
    return prob_coordinate_dict, profile_data_dict