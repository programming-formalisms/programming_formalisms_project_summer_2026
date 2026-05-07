import os

# def divide_by(numerator, denominator):
#     assert isinstance(numerator, (float, int))
#     assert isinstance(denominator, (float, int))
#     assert type(numerator) == type(denominator)
#     assert denominator != 0.0
#     return numerator / denominator


# divide_by(3.0, 4.0)


# def read_file(filename):
#     assert os.path.isfile(filename)
#     assert os.access(filename, os.R_OK)
#     file = open(filename, "r")
#     content = file.read()
#     file.close()
#     return content


# def read_non_empty_file(filename):
#     import os

#     assert os.path.isfile(filename)
#     # if not os.path.exists(filename):
#     #     raise ValueError("File does not exists!")
#     # if not os.path.isfile(filename):
#     #     raise ValueError("Path is not a valid file!")
#     assert os.access(filename, os.R_OK)

#     file = open(filename, "r")
#     content = file.read()
#     assert len(content) > 0
#     if len(content) == 0:
#         raise ValueError("File has no content")
#     file.close()
#     return content


# read_non_empty_file("stefan")


# import weather

# assert not file_exists("figure.png")
# assert not file_exists("statistics_results.txt")

# weather.do_experiment()

# assert file_exists("figure.png")
# assert file_exists("statistics_results.txt")


def do_experiment(filname):
    import os

    # Read the data
    assert os.path.isfile(filename)
    assert os.path.access(filename, os.R_OK)
    # Do the statistics
    # Save the statistics results to file
    assert file_exists("statistics_results.txt")
    # Create the figure
    # Save the figure to file
    assert file_exists("figure.png")
