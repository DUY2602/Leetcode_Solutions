class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        for i in [2, 3, 5]:
            if n % i == 0:
                return self.isUgly(n // i)
        
        return False
