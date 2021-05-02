from Parser import Parser
import argparse
from Instructions import Assembly_Binary


"""
Look at Parser.py for the implementation
"""
def step1():
    # Cleaning the file: Removing whitespaces, empty lines, comments etc
    parser = argparse.ArgumentParser()
    parser.add_argument('Path', type=str, help="drag your file here")
    path = parser.parse_args().Path
    return Parser(path).clean_file(),path


"""
Look at Instructions.py for the implementation
"""
def step2(parsed_array):
	#Converting Lines to Binary
    return Assembly_Binary(parsed_array).main()


parsed_array,path = step1() #Calling the step 1 function which will clean our file and return an array with all the lines

"""
The parsed array returns an array of array, so we are just chaning it back to 1D array
"""
new_array = []
for each in parsed_array:
	for i in each:
		new_array.append(i)

#Step2 This will create array of binary values
binary_array = step2(new_array)

"""
Now we take the path of our input file and create a path for the output file. We need this so that our output file is in the same folder as input file with the same name
"""
path_array = path.split("/") #This will create an array with all the directorues in the path of the input file
output_name = path_array[-1].split(".") #take the last value in array which is the name of our file and spit it with name and extension
path_array[-1] = f"{output_name[0]}.hack" #we take the name of the file and add .hack to it, to create our output hack file
output_name = ""
#Then we just combine all the previous folders to create a proper path to the file
for each in path_array:
	if each:
		output_name = output_name + "/" + each

"""
The below code, will reject any empty folders and create a file with each line containing the binary values from out array
"""
with open(output_name, "w") as f:
    for line in binary_array:
        string = ""
        for each in line:
            string += str(each)
        f.write("".join(string) + "\n")
