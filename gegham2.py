# Task 2

#
# Create a class given the string, check if it is a palindrome.
# word should be lowercase and 1 ≤ inputString.length ≤ 105
# Example
# For inputString = "aabaa", the output should be true;
# For inputString = "abac", the output should be false;
# For inputString = "a", the output should be true.



class Palindrome:
    def __init__(self, word: str):
        self.word = word

    def validate_word(self):
        if not (1 <= len(self.word) <= 105 and self.word.islower()):
            raise ValueError('wrong word')

    def is_palindrome(self) -> bool:
        return self.word[::-1] == self.word

    def run(self):
        self.validate_word()
        return self.is_palindrome()


x = Palindrome("aaa")
print(x.run())
