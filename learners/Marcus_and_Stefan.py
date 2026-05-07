import os
import matplotlib
import matplotlib.pyplot as plt

def file_exists(file_path):
    """
    Check if input file exists
     returns True of file exists, else return False
    """
    # Check if file exists
    return os.path.exists(file_path)
   
def generate_figure(data):
    """
    Generates plot
    """
    # Plot data
    fig = plt.figure()
    plt.savefig("/Users/wenne/Documents/programing_formalisms/programming_formalisms_project_summer_2026/learners/grp6_nicolas_marcus/figure.png")
    pass

def clean_data(raw_data):
    # Divide data into summer and winter 

    pass

def create_statisics_file(input_file, output_path):
    """
    The statistics will be performed by focus on the wealth data during the summer and winter, 
    generate a data frame with P valve and regression data. 
    """
    with open(output_path, 'w') as fp:
        return 

def do_experiment():
    """
    Perform experiment
    """
    # Read the data
    # Do the statistics
    # Save the statistics results to file
    data = 0
    # Create the figure
    generate_figure(data)
    create_statisics_file(data, "/Users/wenne/Documents/programing_formalisms/programming_formalisms_project_summer_2026/learners/grp6_nicolas_marcus/statistics_results.txt")

    # Save the figure to file
    
    return 

do_experiment()
assert do_experiment.__doc__
assert file_exists.__doc__
assert generate_figure.__doc__
assert create_statisics_file.__doc__
assert file_exists("/Users/wenne/Documents/programing_formalisms/programming_formalisms_project_summer_2026/learners/grp6_nicolas_marcus/figure.png")
assert file_exists("/Users/wenne/Documents/programing_formalisms/programming_formalisms_project_summer_2026/learners/grp6_nicolas_marcus/statistics_results.txt")
