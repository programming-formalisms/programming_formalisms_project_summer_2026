# Felix do_experiment()

# do_experiment() # Should return a figure and a txt file

def create_png(a):
    """Create a png file."""
    with open(a, "w") as f:
        f.writelines("This should be a figure!")
    pass

assert create_png.__doc__

def create_statistics(a):
    """Create a txt file."""
    with open(a, "w") as f:
        f.writelines("This should contain statistics!")
    pass

assert create_statistics.__doc__

def file_exists(a):
    """Return True if a file exists, else False."""
    import os
    if os.path.isfile(a):
        return True

assert file_exists.__doc__

def do_experiment(a, b):
    """Take a .dat file as input, return a figure and a statistics file."""
    create_png(a) # Create a png file
    create_statistics(b) # Create a statistics .txt file
    

do_experiment("felix_figure.png", "felix_statistics.txt")

assert do_experiment.__doc__
assert file_exists("felix_figure.png")
assert file_exists("felix_statistics.txt")

with open("felix_figure.png") as f:
    lines = f.readlines()
assert len(lines)>0

with open("felix_statistics.txt") as f:
    lines = f.readlines()
assert len(lines)>0

with open("felix_statistics.txt") as f:
    lines = f.readlines()
    
assert 'mean' in lines[0]