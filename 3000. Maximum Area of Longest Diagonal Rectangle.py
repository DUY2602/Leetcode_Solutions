class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_dl = 0
        max_area = 0

        for dimension in dimensions:
            l, w = dimension[0], dimension[1]
            current_dl = l**2 + w**2
            current_area = l * w

            if current_dl > max_dl:
                max_dl = current_dl
                max_area = current_area
            elif current_dl == max_dl:
                max_area = max(max_area, current_area)
        
        return max_area
