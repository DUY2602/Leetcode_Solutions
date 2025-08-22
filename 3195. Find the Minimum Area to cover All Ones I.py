class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        i_coors = []
        j_coors = []
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                if grid[i][j] == 1:
                    j_coors.append(j)
                    i_coors.append(i)

        return ((max(i_coors)-min(i_coors) + 1)*(max(j_coors)-min(j_coors) + 1))
