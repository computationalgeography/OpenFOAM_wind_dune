
import numpy as np
from stl import mesh
import pandas as pd

# Load the STL file
stl_file = 'ground.stl'
stl_mesh = mesh.Mesh.from_file(stl_file)

# Extract the coordinates
x = stl_mesh.x.flatten()
y = stl_mesh.y.flatten()
z = stl_mesh.z.flatten()

# Create a Pandas DataFrame to store the coordinates
data = {'x': x, 'y': y, 'z': z}
df = pd.DataFrame(data)

# Save the coordinates to an Excel file
excel_file = 'path/to/your/output/file.xlsx'
df.to_excel(excel_file, index=False)
