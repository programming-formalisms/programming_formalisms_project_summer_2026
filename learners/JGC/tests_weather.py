import sys

sys.path.insert(0, "../")  # add Folder_2 path to search list
from inspect import getmembers, isfunction

import weather

print(getmembers(weather, isfunction))


#weather.do_analysis()
#assert file_exists("figure.png")
#assert file_exists("statistics_results.txt")
