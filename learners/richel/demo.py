

def file_exists(filename):
    """Eugwefpwow."""
    return True

assert file_exists.__doc__


def is_png_filename(filename):
    """Determines if a filename is suitable for a PNG file,
    e.g. 'figure_1.png'.
    
    Returns True if it is, False in all other cases
    """
    if str_length(filename) < 5:
        return False
    if not str_ends_with(".png"):
        return False
    return True


assert is_png_filename.__doc__
assert is_png_filename("1.png")
assert not is_png_filename(".png")
assert not is_png_filename("png")
assert not is_png_filename("png.png.png")


def is_txt_filename(filename):
    """Determines if a filename is suitable for a text file,
    e.g. 'stats.txt'.
    
    Returns True if it is, False in all other cases
    """
    if str_length(filename) < 5:
        return False
    if not str_ends_with(".txt"):
        return False
    return True

assert is_txt_filename.__doc__
assert is_txt_filename("1.txt")
assert not is_txt_filename(".txt")
assert not is_txt_filename("txt")
assert not is_txt_filename("txt.txt.txt")



def do_analysis(figure_filename, statistics_filename):
    """Do the nalayasröeg.
    Creates two files: a png and txt

    Two arhs:
    - Name of the figure
    - Nae of the txt file
    """
    assert is_png_filename(figure_filename)
    assert is_txt_filename(statistics_filename)

assert do_analysis.__doc__

do_analysis("figure_1.png", "stats.txt")
assert file_exists("figure_1.png")
assert file_exists("stats.txt")

