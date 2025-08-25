class Solution:
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return []
        
        n, m = len(matrix), len(matrix[0])
        
        result, intermediate = [], []
        
        for d in range(n + m - 1):
            
            intermediate.clear()
            
            row, col = 0 if d < m else d - m + 1, d if d < m else m - 1
            
            while row < n and col > -1:
                intermediate.append(matrix[row][col])
                row += 1
                col -= 1
            
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result        
