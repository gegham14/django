# Task 6


# Create a class: Some people are standing in a row in a park. There are trees
# between them which cannot be moved. Your task is to rearrange the people by their
# heights in a non-descending order without moving the trees. People can be very tall!
# Example
#  For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
#  sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].



class High:
    def __init__(self, the_list):
        self.the_list = the_list

    def list_sort(self):
        new_list = []
        for i in self.the_list:
            if i != -1:
                new_list.append(i)

        new_list.sort()
        print(new_list)
        counter = 0
        for i in range(len(self.the_list)):
            if self.the_list[i] != -1:
                self.the_list[i] = new_list[counter]
                counter += 1

        return self.the_list


x = High([-1, 150, 190, 170, -1, -1, 160, 180])
print(x.list_sort())