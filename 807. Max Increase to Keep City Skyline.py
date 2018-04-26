class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowmax = []
        colmax = []

        total = 0
        for i in range(len(grid)):
            rowmax.append(max(grid[i]))
        for i in range(len(grid[0])):
            coltempmax = 0
            for j in range(len(grid)):
                coltempmax = max(coltempmax, grid[j][i])
            colmax.append(coltempmax)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(rowmax[i], colmax[j]) - grid[i][j]
        return total