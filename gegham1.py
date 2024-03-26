# Task 1
#
# Create a class which given a year, return the century
# it is in. The first century spans from the year 1 up to
# and including the year 100, the second - from the
# year 101 up to and including the year 200, etc.
# For year = 1900, the output should be = 19



class YearToCentury:
    def __init__(self, year: int):
        self.year = year

    def the_century(self):
        century = self.year // 100
        # century = self.year % 100
        # if century == 0:
        #     return
        # else:
        #     return self.year // 100 + 1
        return century if not self.year % 100 else century + 1


y = YearToCentury(1900)
print(y.the_century())
