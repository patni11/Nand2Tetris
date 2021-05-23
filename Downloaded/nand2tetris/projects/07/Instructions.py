class VMAssembly:
    def __init__(self, input_array):
        self.final_array = []
        self.input_array = input_array
        self.label_counter = 1
        self.memory_segments = {
            'local': "LCL", 'argument': 'ARG', 'this': 'THIS', 'that': 'THAT', 'temp': '5'}

    def main(self):
        for arr in self.input_array:
            if len(arr) == 1:
                self.arithmetic_operation(arr[0])
            else:
                if arr[1] in self.memory_segments.keys():
                    self.handle_memory_segments(arr)

                else:
                    if arr[1] == 'constant':
                        self.handle_constant(arr)

                    elif arr[1] == 'static':
                        self.handle_static(arr)

                    elif arr[1] == 'pointer':
                        self.handle_pointer(arr)

        return self.final_array

    def handle_pointer(self, arr):
        pass

    def handle_static(self, arr):
        pass

    def arithmetic_operation(self, operation):
        if operation == "eq":
            print("1")
            self.ltgteq(operation)

        elif operation == "add" or "sub":
            if operation == "add":
                self.add()
            else:
                self.sub()

        elif operation == "neg":
            self.neg()

        elif operation == "gt":
            self.ltgteq(operation)

        elif operation == "lt":
            self.ltgteq(operation)

        elif operation == "and":
            self.andor(operation)

        elif operation == "or":
            self.andor(operation)

        elif operation == "not":
            self.nott()

    def handle_constant(self, arr):
        self.final_array.append(f"@{arr[2]}")
        self.final_array.append("D=A")
        self.final_array.append("@SP")
        self.final_array.append("A=M")
        self.final_array.append("M=D")
        self.push()

    def handle_memory_segments(self, arr):
        pass

    def nott(self):
        self.pop()
        self.final_array.append("A=M")
        self.final_array.append("M=!M")
        self.push()

    def andor(self, operation):
        self.top_two_elements()

        if operation == "and":
            self.final_array.append("M=M&D")
        elif operation == "or":
            self.final_array.append("M=M|D")

        self.push()

    def ltgteq(self, operation):
        self.sub()
        self.pop()
        self.final_array.append("A=M")
        self.final_array.append("D=M")
        self.final_array.append(f"@TRUE{self.label_counter}")

        if operation == "gt":
            self.final_array.append("D;JLT")
        elif operation == "lt":
            self.final_array.append("D;JGT")
        if operation == "eq":
            self.final_array.append("D;JEQ")

        self.false()
        self.final_array.append(f"@CONT{self.label_counter}")
        self.final_array.append("D;JMP")
        self.final_array.append(f"(TRUE{self.label_counter})")
        self.true()
        self.final_array.append(f"(CONT{self.label_counter})")
        self.push()
        self.label_counter += 1

    def false(self):
        self.final_array.append("@SP")
        self.final_array.append("A=M")
        self.final_array.append("M=0")

    def true(self):
        self.final_array.append("@SP")
        self.final_array.append("A=M")
        self.final_array.append("M=1")

    def top_two_elements(self):
        self.pop()
        self.final_array.append("A=M")
        self.final_array.append("D=M")
        self.pop()
        self.final_array.append("A=M")

    def add(self):
        self.top_two_elements()
        self.final_array.append("M=D+M")
        self.push()

    def sub(self):
        self.top_two_elements()
        self.final_array.append("M=M-D")
        self.push()

    def neg(self):
        self.pop()
        self.final_array.append("A=M")
        self.final_array.append("M=-M")
        self.push()

    def push(self):
        self.final_array.append("@SP")
        self.final_array.append("M=M+1")

    def pop(self):
        self.final_array.append("@SP")
        self.final_array.append("M=M-1")


"""
    def gt(self):
        self.sub()
        self.pop()
        self.final_array.append("A=M")
        self.final_array.append("D=M")
        self.final_array.append(f"@TRUE{self.label_counter}")
        self.final_array.append("D;JLT")
        self.false()
        self.final_array.append(f"@CONT{self.label_counter}")
        self.final_array.append("D;JMP")
        self.final_array.append(f"(TRUE{self.label_counter})")
        self.true()
        self.final_array.append(f"(CONT{self.label_counter})")
        self.push()
        self.label_counter += 1

    def lt(self):
        self.sub()
        self.pop()
        self.final_array.append("A=M")
        self.final_array.append("D=M")
        self.final_array.append(f"@TRUE{self.label_counter}")
        self.final_array.append("D;JGT")
        self.false()
        self.final_array.append(f"@CONT{self.label_counter}")
        self.final_array.append("D;JMP")
        self.final_array.append(f"(TRUE{self.label_counter})")
        self.true()
        self.final_array.append(f"(CONT{self.label_counter})")
        self.push()
        self.label_counter += 1

    def equal(self):
        self.sub()
        self.pop()
        self.final_array.append("A=M")
        self.final_array.append("D=M")
        self.final_array.append(f"@TRUE{self.label_counter}")
        self.final_array.append("D;JEQ")
        self.false()
        self.final_array.append(f"@CONT{self.label_counter}")
        self.final_array.append("D;JMP")
        self.final_array.append(f"(TRUE{self.label_counter})")
        self.true()
        self.final_array.append(f"(CONT{self.label_counter})")
        self.push()
        self.label_counter += 1
"""
