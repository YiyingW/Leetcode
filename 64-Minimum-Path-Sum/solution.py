
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

        for i in range(1, ncol):
            for j in range(1, nrow):
                path[(i, j)] = min(path[(i-1,j)], path[(i, j-1)], path[(i-1, j-1)])
        return path[(nrow-1, ncol-1)]
