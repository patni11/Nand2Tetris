class Assembly_Binary:
    def __init__(self, input_array):
        self.input_array = input_array
        self.final_array = []
        self.binary_array = []
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

        self.destination_dict = {"M": "0 0 1", "D": "0 1 0", "MD": "0 1 1", "A": "1 0 0", "AM": "1 0 1",
                                 "AD": "1 1 0", "AMD": "1 1 1"}

        self.jump_dict = {"JGT": "0 0 1", "JEQ": "0 1 0", "JGE": "0 1 1", "JLT": "1 0 0",
                          "JNE": "1 0 1", "JLE": "1 1 0", "JMP": "1 1 1"}

        self.symbols_dict = {"R0": "0", "R1": "1", "R2": "2", "R3": "3", "R4": "4", "R5": "5", "R6": "6", "R7": "7", "R8": "9", "R10": "10", "R11": "11", "R12": "12",
                             "R13": "13", "R14": "14", "R15": "15", "SCREEN": "16384", "KBD": "24576", "SP": "0", "LCL": "1", "ARG": "2", "THIS": "3", "THAT": "4"}

        self.variable_counter = 16

    def main(self):
        initial_array = self.input_array
        for each in initial_array:
            instruction = self.AorC(each)
            if instruction == "A":
                self.final_array.append(self.handle_A_instruction(each))

            elif instruction == "C":
                self.handle_C_instruction(each)
                self.final_array.append(self.binary_array)

                self.binary_array = []

            elif instruction == "LABEL":
                string = each.replace('(', "")
                string = string.replace(')', "")
                if string not in self.symbols_dict.keys():
                    self.symbols_dict[string] = len(self.final_array) - 1

        return self.final_array

    def handle_C_instruction(self, each):
        self.binary_array = [1, 1, 1]

        if "=" in each:
            array = each.split("=")
            if ";" in array[1]:
                second_array = array[1].split(";")
                self.c_operation(second_array[0])
                self.destination(array[0])
                self.jump(second_array[1])
                return
            else:
                self.c_operation(array[1])
                self.destination(array[0])
                self.binary_array.append(0)
                self.binary_array.append(0)
                self.binary_array.append(0)
                return

        if ";" in each:
            array = each.split(";")
            self.c_operation(array[0])
            self.binary_array.append(0)
            self.binary_array.append(0)
            self.binary_array.append(0)
            self.jump(array[1])
            return

    def c_operation(self, array):
        for each in self.c_operation_dict[array].split(" "):
            self.binary_array.append(int(each))

    def destination(self, array):
        for each in self.destination_dict[array].split(" "):
            self.binary_array.append(int(each))

    def jump(self, array):
        for each in self.jump_dict[array].split(" "):
            self.binary_array.append(int(each))

    def handle_A_instruction(self, each):
        if isinstance(each, str):
            new_string = each.replace('@', '')
            try:
                number = int(new_string)
            except:
                if new_string not in self.symbols_dict.keys():
                    self.symbols_dict[new_string] = str(self.variable_counter)
                    self.variable_counter += 1

                number = int(self.symbols_dict[new_string])

        self.convert_to_binary(number)

        while len(self.binary_array) < 16:
            self.binary_array.append(0)

        new_array = []
        for i in range(len(self.binary_array)-1, -1, -1):
            new_array.append(self.binary_array[i])

        self.binary_array = []
        return new_array

    def convert_to_binary(self, number):
        if number == 1:
            self.binary_array.append(1)
            return
        elif number == 0:
            self.binary_array.append(0)
            return

        self.binary_array.append(number % 2)
        self.convert_to_binary(number // 2)

    def AorC(self, each):
        if each[0] == "@":
            return "A"
        elif each[0] == "(":
            return "LABEL"
        else:
            return "C"
