import weather

weather.do_experiment()

assert file_exists("figure.png")
assert file_exists("statistics_results.txt")



# Exercise 3.6
def do_experiment():
  # Read the data
  data = load_data()
  assert len(data) > 0
  # Do the statistics
  # Save the statistics results to file
  # Create the figure
  # Save the figure to file



# Our solution (exercise 3.5)
def do_experiment(filename):
    # Check if file exists and contains data
    data = load_data(filename)
    # Check if data is loaded
    statistics = do_data_analysis(data)
    # Check statistics is not empty
    plot_data(statistics)
    # Check if plot is saved
    return True
