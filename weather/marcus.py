"""
This is marcus test script. Lets fix it!
"""

import os
import matplotlib.pyplot as plt

list_path = ["/Users/wenne/Documents/programing_formalisms/", 
    "programming_formalisms_project_summer_2026/learners/grp6_nicolas_marcus/statistics_results.txt"]
path_stats_out =  "".join(list_path)

list_path_fig = ["/Users/wenne/Documents/programing_formalisms/", 
                     "programming_formalisms_project_summer_2026/", 
                     "learners/grp6_nicolas_marcus/figure.png"]
path_fig_out = "".join(list_path_fig)

def file_exists(file_path):
    """
    Check if input file exists.

    Returns True of file exists, else return False.
    """

    # Check if file exists
    return os.path.exists(file_path)
   
def generate_figure(data):
    """Generate plot."""
    # Plot data
    plt.figure(data)
    plt.savefig(path_fig_out)

def clean_data():
    """
    Divide the data into mean temperature for the summer and winter each complete year in Uppsala.

    Summer = Jun - Aug.
    Winter = Nov - Feb.
    """
    # Divide data into summer and winter

def create_statisics_file(data, output_path):
    """
    Generate statiscs.
    
    The statistics will be performed by focus on the wealth
    data during the summer and winter, generate
    a data frame with P valve and regression data.
    """

    with open(output_path, "w") as fp:
        fp.write(data)

def do_experiment():
    """Perform experiment."""
    # Read the data
    # Do the statistics
    # Save the statistics results to file
    data = 0
    # Create the figure
    generate_figure(data)
    create_statisics_file(data, path_stats_out)
    # Save the figure to file 

do_experiment()
assert do_experiment.__doc__
assert file_exists.__doc__
assert generate_figure.__doc__
assert create_statisics_file.__doc__
assert clean_data.__doc__
assert file_exists(path_stats_out)
assert file_exists(path_fig_out)
