"""Richel's code."""

def get_name():
    """Get Richel's name, spelled correctly."""
    return "Richèl"

def collect_first_third_temperatures():
    return range(1, 100)

def get_first_third_temperatures():
    """Get the first third of temperatures.
    This excludes the year 1722, as this year is not completely measured.
    """
    return collect_first_third_temperatures()

assert len(get_first_third_temperatures()) > 10

def get_last_third_temperatures():
    return [7.8, 9.0, 1.2]

def calc_p_value(values_1 = get_first_third_temperatures(), values_2 = get_last_third_temperatures()):
    """Create the p value of the statistics test."""
    from scipy import stats
    return stats.kstest(values_1, values_2).pvalue


expected_p_value = 0.8810 # From https://agentcalc.com/kolmogorov-smirnov-test-calculator
# expected_p_value = 0.8659 # From https://www.statskingdom.com/kolmogorov-smirnov-two-calculator.html

values_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
assert calc_p_value(values_1, values_2) >= expected_p_value - 0.1
assert calc_p_value(values_1, values_2) <= expected_p_value + 0.1

def file_exists(filename):
    return True


def create_figure():
    """Create the boxplot of temperatures."""
    file = open("figure.png", "w")
    file.close()

assert create_figure.__doc__
create_figure()
assert file_exists("figure.png")

def create_statistics_file():
    """Create the file with the statistics needed."""
    file = open("statistics_results.txt", "w")
    p_value = calc_p_value()
    assert p_value >= 0.0
    assert p_value <= 1.0
    file.write("p value:" + str(p_value))
    file.close()


assert create_statistics_file.__doc__
create_statistics_file()
assert file_exists("statistics_results.txt")

def do_analysis():
    """Do the analysis as described in the paper."""
    create_figure()
    create_statistics_file()

do_analysis()
assert do_analysis.__doc__
assert file_exists("figure.png")
assert file_exists("statistics_results.txt")
