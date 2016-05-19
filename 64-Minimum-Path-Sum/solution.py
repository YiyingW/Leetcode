class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrow = len(grid)
        ncol = len(grid[0])
        path = {}
        for i in range(0, ncol):
            path[(0, i)] = grid[0][i]
        for i in range(0, nrow):
            path[(i, 0)] = grid[i][0]

        if ncol > 1 and nrow > 1:
            for i in range(1, ncol):
                for j in range(1, nrow):
                    path[(i, j)] = min(path[(i-1,j)], path[(i, j-1)], path[(i-1, j-1)])
            return path[(nrow, ncol)]
        elif ncol > 1:
            return path[(0, ncol)]
        elif nrow > 1:
            return path[(nrow, 0)]
        else:
            return path[(0,0)]
