class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrow = len(grid)
        ncol = len(grid[0])
        path = {}
        path[(0,0)] = grid[0][0]

        for i in range(1, ncol):
            path[(0, i)] = path[(0,i-1)] + grid[0][i]
        for i in range(1, nrow):
            path[(i, 0)] = path[(i-1, 0)] + grid[i][0]

        for i in range(1, nrow):
            for j in range(1, ncol):
                path[(i, j)] = min(path[(i-1,j)], path[(i, j-1)]) + grid[i][j]
        return path[(nrow-1, ncol-1)]

