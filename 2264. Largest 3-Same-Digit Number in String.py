class Solution:
    def largestGoodInteger(self, num: str) -> str:
        target = ""
        for i in range(0, 10):
            if (str(i) * 3) in num:
                target = str(i) * 3

        return target
