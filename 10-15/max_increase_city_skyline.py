class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        
        # Problem boils down to getting the maximum element in a certain 'T Section' of the grid
        # For example with the grid:
        # 3 0 8 4
        # 2 4 5 7
        # 9 2 6 3
        # 0 3 1 0
        # And then taking the minimum of each, and increasing every element of the T by that ammount
        
        rows = len(grid)
        cols = len(grid[0])
        
        # Keep track of the max of each row and column
        maxRows = [0] * rows
        maxCols = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                # The max number in row i is the the maximum between the current element and our current max
                maxRows[i] = max(grid[i][j], maxRows[i])
                # The max number in column j is the the maximum between the current element and our current max
                maxCols[j] = max(grid[i][j], maxCols[j])
        
        # Tally the sum of differences
        # Take the minimum between the maxRows[i] and maxCols[j] because if we took the maximum we would go over
        # the skyline and get an incorrect answer
        return sum([min(maxRows[i], maxCols[j]) - grid[i][j] for i in range(rows) for j in range(cols)])
