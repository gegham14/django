# # Task 4
#
# Create a class which given a list of strings, return another list containing
# all of its longest strings.
# Example
# For inputList = ["aba", "aa", "ad", "vcd", "aba"],
# the output should be
#  allLongestStrings(inputList) = ["aba", "vcd", "aba"].



class HighestWord:
    def __init__(self, the_list: list) -> list:
        self.the_list = the_list

    def the_longest(self):
        empty_list = []
        self.the_list = sorted(self.the_list)

        max_length = len(self.the_list[0])

        for i in range(len(self.the_list)):
            if len(self.the_list[i]) > max_length:
                max_length = len(self.the_list[i])
        for i in range(len(self.the_list)):
            if len(self.the_list[i]) == max_length:
                empty_list.append(self.the_list[i])
        return empty_list


x = HighestWord(['z', 'barev', "che", "ba", "jan", "che", "xi"])
print(x.the_longest())
