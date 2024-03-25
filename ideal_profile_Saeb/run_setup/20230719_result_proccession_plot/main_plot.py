
import sys

import plot_to_docx

if len(sys.argv) < 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
   
    print ("result_file_directory ")   

    sys.exit(0)

plot_directory = sys.argv[1]

'''plots save in word file'''
# Read the figures from the directory

figures = plot_to_docx.read_figures_from_directory(plot_directory)

# Specify the output Word file
word_file = 'output.docx'

# Create the Word file with the figures
plot_to_docx.create_word_file(figures, word_file)


