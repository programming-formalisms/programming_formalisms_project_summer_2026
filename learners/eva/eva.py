################ Exercise 6 ########################
import pandas as pd


def read_non_empty_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    #file = open(filename, "r")
    #content = file.read()
    #file.close()
    #column_names = ['Year', 'Months', 'Day', 'Avg_temp', 'Avg_temp_corrected', 'Data_id_no']
    content = pd.read_csv(filename, delimiter="\t")#, names=column_names)
    assert isinstance(content, pd.DataFrame)
    return content

def do_experiment():
  # Read the data
  data_file = r"C:\Users\EVAK\OneDrive - Umeå universitet\Courses\2026_ProgrammingFormalisms\programming_formalisms_project_summer_2026\data\uppsala_tm_1722-2022.dat"
  content = read_non_empty_file(data_file)
  # Do the statistics
  # Save the statistics results to file
  assert file_exists("figure.png")
  # Create the figure
  # Save the figure to file
  assert file_exists("statistics_results.txt")


data_file = r"C:\Users\EVAK\OneDrive - Umeå universitet\Courses\2026_ProgrammingFormalisms\programming_formalisms_project_summer_2026\data\uppsala_tm_1722-2022.dat"
content = read_non_empty_file(data_file)
print(content.columns)
assert (content.columns ==  ["Year", "Months", "Day", "Avg_temp", "Avg_temp_corrected", "Data_id_no"]).all()


##################### Exerecise 2 ################

def is_even(num):
    """Check if input number is even. Retrun True is number is even, otherwise false. Raises an error when input is not a number.
    """
    if not isinstance(num, int):
        raise TypeError("'num' must be of type int")

    if (num%2)==0:
        return True
    return False

assert is_even.__doc__
assert is_even(2)
assert not is_even(3)

has_thrown = False
try:
    is_even(0.0)
except TypeError:
    has_thrown = True
assert has_thrown


################ Exercise 3 ###################
def is_odd(num):
    """Check if input number is odd. Return True if number is odd, else False. Raises a TypeError for invalid input.
    """
    return not is_even(num)

assert is_odd.__doc__
assert is_odd(3)
#assert not is_odd(2) #not valid test since it already passes

############## Exercise 4 ################

def is_prime(num):
    """Checks if a number is a prime number. Return True is input is prime number, else False. Raises Type Error if input is not int
    """
    if not isinstance(num, int):
        raise TypeError("'num' must be of type int")

    def Prime(no, i):
        if no == i:
            return True
        if no % i == 0:
            return False
        return Prime(no, i + 1)

    return Prime(num, 2)

assert is_prime.__doc__
assert is_prime(5)
assert not is_prime(4)

has_thrown = False
try:
    is_prime(0.0)
except TypeError:
    has_thrown = True
assert has_thrown






############## Exercise 1 ######################
def is_zero(num):
    """Check if input is zero. Return True if zero, False otherwise, Raises error if not a number.
    """
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be of type int or float")

    if num == 0:
        return True
    return False

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(10)

has_thrown = False
try:
    is_zero("nonsense")
except:
    has_thrown = True
assert has_thrown
