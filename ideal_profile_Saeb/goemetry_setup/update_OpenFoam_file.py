import os
import re

def extract_vector(line):
    # Define the regular expression pattern to match the vector values
    pattern = r"\((-?\d+(?:\.\d+)?(?:\s+-?\d+(?:\.\d+)?){2})\)"

    # Search for the vector pattern in the line
    match = re.search(pattern, line)

    if match:
        # Extract the vector values from the matched pattern
        vector_values = match.group(1).split()
        return [float(value) for value in vector_values]

    return None

def update_file(input_file, output_file, keywords):
    # Read the contents of the input file
    with open(input_file, 'r') as file_a:
        a_contents = file_a.readlines()

    # Read the contents of the output file
    with open(output_file, 'r') as file_b:
        b_contents = file_b.readlines()

    # Find the indices of the lines containing the keywords in the output file
    keyword_indices = {keyword: None for keyword in keywords}

    for i, line in enumerate(b_contents):
        for keyword in keywords:
            if keyword in line and f'${keyword}' not in line:
                keyword_indices[keyword] = i
                break

    # Extract the values from the input file
    keyword_values = {}
    for keyword in keywords:
        for line in a_contents:
            if keyword in line:
                values = extract_vector(line)
                if values:
                    keyword_values[keyword] = values
                    break
                else:
                    values = line.split()[1]
                    keyword_values[keyword] = values

    # Update the values in the output file
    for keyword in keywords:
        index = keyword_indices[keyword]
        values = keyword_values[keyword]

        if index is not None and values is not None:
            if isinstance(values, list):
                b_contents[index] = f"{keyword} ({' '.join(map(str, values))});\n"
            else:
                b_contents[index] = f"{keyword} {values};\n"

    # Write the updated contents back to the output file
    with open(output_file, 'w') as file_b:
        file_b.writelines(b_contents)
