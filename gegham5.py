# Task 5
# Ticket numbers usually consist of an even number of digits.A ticket number is
# considered lucky if the sum of the first half of the digits is equal to the sum of the
# second half.Given a ticket number n, determine if it's lucky or not. Example For n
# = 1230, the output should be
# Lucky(n) = true;
# For n = 239017,
# the output should be Lucky(n) = false


class Lucky:
    def __init__(self, num: int):
        self.num = num

    def lucky_ticket(self):
        if len(str(self.num)) % 2 != 0:
            raise ValueError('odd number')

        else:
            str_num = str(self.num)
            mid = len(str_num) // 2
            c = [int(i) for i in str_num]
            return sum(c[mid:]) == sum(c[:mid])


x = Lucky(2320)
print(x.lucky_ticket())
