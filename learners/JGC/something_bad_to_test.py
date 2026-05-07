file = "../data/uppsala_tm_1722-2022.txt"

with open(file) as f:
    print(f.read())

assert type(file) == str 