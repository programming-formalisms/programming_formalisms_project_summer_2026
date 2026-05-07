def divide_by(numerator, denominator):
    assert denominator != 0
    assert not isinstance(denominator, complex) and not isinstance(numerator, complex)
    assert isinstance(denominator,(int,float)) and isinstance(numerator,(int,float))
    return (numerator / denominator)

filename = "/Users/pe4666st/NBIS_project2026/programming_formalisms_project_summer_2026/src/learners/README.md"
filename = "/Users/pe4666st/NBIS_project2026/programming_formalisms_project_summer_2026/src/learners/README0001.md"

def read_file(filename):
    from pathlib import Path
    assert Path(filename).is_file()
    file = open(filename)
    content = file.read()
    file.close()
    return content

text = read_file(filename)
print(text.splitlines()[0])
