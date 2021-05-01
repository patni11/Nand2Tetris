from Parser import Parser
import argparse
from Instructions import Assembly_Binary


def step1():
    # Cleaning the file: Removing whitespaces, empty lines, comments etc
    parser = argparse.ArgumentParser()
    parser.add_argument('Path', type=str, help="drag your file here")
    path = parser.parse_args().Path
    return Parser(path).clean_file(),path


def step2(parsed_array):
    return Assembly_Binary(parsed_array).main()


parsed_array,path = step1()
new_array = []
for each in parsed_array:
	for i in each:
		new_array.append(i)

binary_array = step2(new_array)

path_array = path.split("/")
output_name = path_array[-1].split(".")
path_array[-1] = f"{output_name[0]}.hack"
output_name = ""
for each in path_array:
	if each:
		output_name = output_name + "/" + each

with open(output_name, "w") as f:
    for line in binary_array:
        string = ""
        for each in line:
            string += str(each)
        f.write("".join(string) + "\n")
