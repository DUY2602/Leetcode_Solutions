class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        if len(str(num)) == 1:
            return num
        for digit in str(num):
            total += int(digit)
        return self.addDigits(total)
