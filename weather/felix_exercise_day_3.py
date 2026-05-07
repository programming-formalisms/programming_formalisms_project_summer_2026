# Felix do_experiment()

# do_experiment() # Should return a figure and a txt file

def create_png(a):
    """Create a png file."""

assert create_png.__doc__

def file_exists(a):
    """Return True if a file exists, else False."""
    import os
    if (os.path.isfile(a) == True):
        return True
    return False

assert file_exists.__doc__

def do_experiment(a):
    """Take a .dat file as input, return a figure and a statistics file."""
    # Create a statistics .txt file
    # Create a png file

do_experiment(1)

assert do_experiment.__doc__
assert file_exists("felix_figure.png")
assert file_exists("felix_statistics.txt")
