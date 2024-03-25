import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_data(data_file, X_label, Y_label, Y_variable, title, save_file):
    # Read the data from the file
    data = pd.read_csv(data_file)

    # Extract the x and y columns
    x = data[X_label]
    variable = data[Y_variable]
    y = data[Y_label]
    
    
    title = title.replace("/", "_")
    title = title.replace("run", "")
    title = title.replace("..", "")
    
    # Plot the profile
    plt.plot(x, y, label='Bed profile', color='r')
    # Plot x against y
    plt.plot(x, variable, label='Velocity', color='b')
    
    plt.xlabel(X_label)
    label_plot_y = f'{Y_variable} and {Y_label}'
    plt.ylabel(label_plot_y)
    plt.title(title)
    
    # Show the legend
    plt.legend()

    # Save the plot as a figure
    save_path = os.path.join(save_file, f'{title}'+"plot.png")
    plt.savefig(save_path)

    # Show the plot
    #plt.show()
    #plt.close()
