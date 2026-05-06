# Script to analyze weather data from Uppsala

def file_exists(s):
    '''
    Check if file exists
    '''
    import os
    return os.path.exists(s)

def do_analysis():
    '''
    Texttext
    '''
    # Read the data
    # Do the statistics
    # Save the statistics results to file
    assert file_exists("figure.png")
    # Create the figure
    # Save the figure to file
    assert file_exists("statistics_results.txt")


assert do_analysis.__doc__
assert file_exists.__doc__
assert not file_exists('sokfsdofjsd')
assert file_exists(r"C:\Users\EVAK\OneDrive - Umeå universitet\Courses\2026_ProgrammingFormalisms\programming_formalisms_project_summer_2026\learners\test.md")
