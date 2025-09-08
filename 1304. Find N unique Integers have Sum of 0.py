class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 != 0:
            result = [0]
        else:
            result = []
        for i in range(1, n //2 + 1):
            result.append(i)
            result.append(-i)

        return result   
            
