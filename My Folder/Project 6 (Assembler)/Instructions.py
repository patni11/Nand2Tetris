
#Our class to convert each line of assembly language to relevant binary code
class Assembly_Binary:
    def __init__(self, input_array):
        self.input_array = input_array
        self.final_array = [] #To store the final 16bit binary lines of the output
        self.binary_array = [] #To store temporary output

        #Dictionary for computation
        self.c_operation_dict = {"0": "0 1 0 1 0 1 0", "1": "0 1 1 1 1 1 1",
                                 "-1": "0 1 1 1 0 1 0", "D": "0 0 0 1 1 0 0",
                                 "A": "0 1 1 0 0 0 0", "!D": "0 0 0 1 1 0 1",
                                 "!A": "0 1 1 0 0 0 1", "-D": "0 0 0 1 1 1 1",
                                 "-A": "0 1 1 0 0 1 1", "D+1": "0 0 1 1 1 1 1",
                                 "A+1": "0 1 1 0 1 1 1", "D-1": "0 0 0 1 1 1 0",
                                 "A-1": "0 1 1 0 0 1 0", "D+A": "0 0 0 0 0 1 0",
                                 "D-A": "0 0 1 0 0 1 1", "A-D": "0 0 0 0 1 1 1",
                                 "D&A": "0 0 0 0 0 0 0", "D|A": "0 0 1 0 1 0 1",
                                 "M": "1 1 1 0 0 0 0", "!M": "1 1 1 0 0 0 1",
                                 "-M": "1 1 1 0 0 1 1", "M+1": "1 1 1 0 1 1 1",
                                 "M-1": "1 1 1 0 0 1 0", "D+M": "1 0 0 0 0 1 0",
                                 "D-M": "1 0 1 0 0 1 1", "M-D": "1 0 0 0 1 1 1",
                                 "D&M": "1 0 0 0 0 0 0", "D|M": "1 0 1 0 1 0 1"}

        #Dictionary for Destination
        self.destination_dict = {"M": "0 0 1", "D": "0 1 0", "MD": "0 1 1", "A": "1 0 0", "AM": "1 0 1",
                                 "AD": "1 1 0", "AMD": "1 1 1"}

        #Dictionary for Jump
        self.jump_dict = {"JGT": "0 0 1", "JEQ": "0 1 0", "JGE": "0 1 1", "JLT": "1 0 0",
                          "JNE": "1 0 1", "JLE": "1 1 0", "JMP": "1 1 1"}

        #Dictionary for Symbols
        self.symbols_dict = {"R0": "0", "R1": "1", "R2": "2", "R3": "3", "R4": "4", "R5": "5", "R6": "6", "R7": "7", "R8": "9", "R10": "10", "R11": "11", "R12": "12",
                             "R13": "13", "R14": "14", "R15": "15", "SCREEN": "16384", "KBD": "24576", "SP": "0", "LCL": "1", "ARG": "2", "THIS": "3", "THAT": "4"}

        #To keep tracck of variables enountered so far
        self.variable_counter = 16

    #main function to implement other operations
    def main(self):
        initial_array = self.input_array
        self.first_pass(initial_array) #First Pass
        self.second_pass(initial_array) #Second pass
        
        for each in initial_array:
            instruction = self.AorC(each) #Check if it is A or C instruction
            
            if instruction == "A":
                self.final_array.append(self.handle_A_instruction(each)) #Perform A operation and store result in final array

            elif instruction == "C":
                self.handle_C_instruction(each) #Perform C operation and 
                self.final_array.append(self.binary_array) #store result in final array

                self.binary_array = [] #Reset the temporary binary array, which stores the calculation for each input array value

        return self.final_array #Final output with all the lines converted to binary

    # TO HANDLE LABELS
    def first_pass(self,initial_array):
        counter = 0 #To keep track of line numbers
        for each in initial_array:
            if "(" in each:  
                string = each.replace('(', "")
                string = string.replace(')', "")
                if string not in self.symbols_dict.keys():
                    self.symbols_dict[string] = counter #Add the label to symbols dictionary with value as the counter. Do this if the line starts with "("
            else:
                counter += 1 #Increase the counter by 1 if we did not encoutner the label. THis is because labels are not counterd as lines in binary

    # TO HANDLE VARIABLES
    def second_pass(self,initial_array):
        for each in initial_array:
            if "@" in each:
                new_string = each.replace("@","")
                # Try to convert it into a integer, if it dosen't work, that means it is a variable
                try:
                    number = int(new_string)
                except:
                    if new_string not in self.symbols_dict.keys():
                        self.symbols_dict[new_string] = str(self.variable_counter) #Storing variable in the symbols dictionary with value as our varible counter
                        self.variable_counter += 1 #increment variable counter by 1

    # TO HANDLE C INSTRUCTIONS
    def handle_C_instruction(self, each):
        self.binary_array = [1, 1, 1] #Set binary array to 111 because C instructions start with it

        #We split the array to two parts before "=" and after "=". Handles arugments like D=M-D;JLE
        if "=" in each:
            array = each.split("=")
            #There is a chance that we have a jump condition. We can split using ";" and handle it
            if ";" in array[1]:
                second_array = array[1].split(";")
                self.c_operation(second_array[0]) #Perfrom computation
                self.destination(array[0]) #Perfrom destination
                self.jump(second_array[1]) #Perfrom jump
                return
            else:
                self.c_operation(array[1])
                self.destination(array[0])
                self.binary_array.append(0)
                self.binary_array.append(0)
                self.binary_array.append(0)
                return
        #We split the array to two parts before ";" and after ";". Handles arugments like D;JLE. We need this in case there is no "=""
        if ";" in each:
            array = each.split(";")
            self.c_operation(array[0])
            self.binary_array.append(0)
            self.binary_array.append(0)
            self.binary_array.append(0)
            self.jump(array[1])
            return

    #Handles computation
    def c_operation(self, array):
        for each in self.c_operation_dict[array].split(" "):
            self.binary_array.append(int(each))

    #Handles Destination
    def destination(self, array):
        for each in self.destination_dict[array].split(" "):
            self.binary_array.append(int(each))

    #Handles Jump
    def jump(self, array):
        for each in self.jump_dict[array].split(" "):
            self.binary_array.append(int(each))

    #HANDLES A INSTRUCTION
    def handle_A_instruction(self, each):
        if isinstance(each, str):
            new_str = each.replace('@', '')
            # if variable, get the value from symbol dictionary else convert the string to integer
            if new_str in self.symbols_dict.keys():
                number = int(self.symbols_dict[new_str])
            else:
                number = int(new_str)

        self.convert_to_binary(number) #Converts the number to binary

        #Add zeros if the length of array is less than 16, we need this because of register size
        while len(self.binary_array) < 16:
            self.binary_array.append(0)

        #Flip the binary array because it stores value in the opposite order
        new_array = []
        for i in range(len(self.binary_array)-1, -1, -1):
            new_array.append(self.binary_array[i])

        self.binary_array = [] #rseset binary array
        return new_array

    #CONVERTS THE NUMBER TO BINARY
    def convert_to_binary(self, number):
        if number == 1:
            self.binary_array.append(1)
            return
        elif number == 0:
            self.binary_array.append(0)
            return

        self.binary_array.append(number % 2)
        self.convert_to_binary(number // 2)

    # CHECK IF WE HAVE A 'C' OR 'A' INSTRUCTION
    def AorC(self, each):
        if each[0] == "@":
            return "A"
        elif each[0] == "(":
            return "IGNORE"
        else:
            return "C"
