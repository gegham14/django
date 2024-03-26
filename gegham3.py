# task 3
#
# Create a Class which given an list of integers, find the pair of
# adjacent elements that has the largest product and return that
# product.
# For inputList = [3, 6, -2, -5, 7, 3],
# the output should be = 21



class MaxNumber:
    def __init__(self, n):
        self.n = n

    def maxProduct(self):
        max_number = self.n[0] * self.n[1]
        for i in range(len(self.n) - 1):
            if self.n[i] * self.n[i + 1] > max_number:
                max_number = self.n[i] * self.n[i + 1]
        return max_number


x = MaxNumber([3, 6, -2, -5, 7, 3])
print(x.maxProduct())
