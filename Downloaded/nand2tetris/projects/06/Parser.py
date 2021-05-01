class Parser:

    def __init__(self, path):
        self.path = path

    def clean_file(self):
        final_array = []
        with open(self.path, 'r') as f:
            for each in f.readlines():
                if each:
                    removed_comments = self.remove_comments(each)
                    if removed_comments:
                        removed_white_space = self.remove_white_spaces(removed_comments)
                        if removed_white_space:
                            final_array.append(removed_white_space)

            final_array = self.clearN(final_array)
            return final_array

    def clearN(self, final):
        final_array = []
        for i in final:
            if i == "\n" or len(i) == 0:
                continue
            else:
                final_array.append(i)

        return final_array

    def remove_white_spaces(self, each):
        array = []
        for i in each:
            i = i.strip()
            if i:
                if "\n" in i:
                    i = i.strip("\n")
                array.append(i)
        return array

    def remove_comments(self, each):
        removed_array = []
        for i in each.split(' '):
            if i != "//":
                removed_array.append(i)
            else:
                return removed_array
        return removed_array


'''
    def save_cleaned_file(self,final_array):
        with open("/Users/xenox/Documents/Coadddding/Nand2Tetris/Downloaded/nand2tetris/projects/06/cleaned.hack","w") as f:
            for line in final_array:
                f.write("".join(line) + "\n")

'''
