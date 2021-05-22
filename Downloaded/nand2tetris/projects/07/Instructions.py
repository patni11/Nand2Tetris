class VMAssembly:
    def __init__(self, input_array):
        self.final_array = []
        self.input_array = input_array

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
        if operation == "add" or "sub":
            self.pop()
            self.final_array.append("A=M")
            self.final_array.append("D=M")
            self.pop()
            self.final_array.append("A=M")
            if operation == "add":
                self.final_array.append("M=D+M")
            else:
                self.final_array.append("M=D-M")
            self.push()

        elif operation == "neg":
            self.pop()
            self.final_array.append("A=M")
            self.final_array.append("M=-M")
            self.push()

        elif operation == "eq":

            pass
        elif operation == "gt":
            pass
        elif operation == "lt":
            pass
        elif operation == "and":
            pass
        elif operation == "or":
            pass
        elif operation == "not":
            pass

    def handle_constant(self, arr):
        self.final_array.append(f"@{arr[2]}")
        self.final_array.append("D=A")
        self.final_array.append("@SP")
        self.final_array.append("A=M")
        self.final_array.append("M=D")
        self.push()

    def handle_memory_segments(self, arr):
        pass

    def push(self):
        self.final_array.append("@SP")
        self.final_array.append("M=M+1")

    def pop(self):
        self.final_array.append("@SP")
        self.final_array.append("M=M-1")
