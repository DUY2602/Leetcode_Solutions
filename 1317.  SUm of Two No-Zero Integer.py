class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            j = n - i
            if str(i).count("0") >= 1 or str(j).count("0") >= 1:
                continue
            else:
                return [i, j]
