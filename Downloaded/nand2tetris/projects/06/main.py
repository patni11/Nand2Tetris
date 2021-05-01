from Parser import Parser
import argparse
from Instructions import Assembly_Binary


def step1():
    # Cleaning the file: Removing whitespaces, empty lines, comments etc
    parser = argparse.ArgumentParser()
    parser.add_argument('Path', type=str, help="drag your file here")
    path = parser.parse_args().Path
    return Parser(path).clean_file()


def step2(parsed_array):
    return Assembly_Binary(parsed_array).main()


parsed_array = step1()
print(parsed_array)
binary_array = step2(parsed_array)

with open("/Users/xenox/Documents/Coadddding/Nand2Tetris/Downloaded/nand2tetris/projects/06/max/Max.hack", "w") as f:
    for line in binary_array:
        string = ""
        for each in line:
            string += str(each)
        f.write("".join(string) + "\n")
