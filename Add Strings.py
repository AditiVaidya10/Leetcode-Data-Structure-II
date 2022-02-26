class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(self.convert(num1)+self.convert(num2))
    def convert(self, string):
        result, digits = 0, {str(i):i for i in range(10)}
        for i in string:
            result = result*10 + digits[i]
        return result
