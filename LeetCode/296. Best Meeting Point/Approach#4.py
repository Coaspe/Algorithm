class Solution:
    def minTotalDistance(self, grid):
        rows, cols = self.collect_rows(grid), self.collect_cols(grid)
        m_r, m_c = rows[len(rows)//2], cols[len(cols)//2]
        return self.minDistance1D(rows, m_r) + self.minDistance1D(cols, m_c)

    def minDistance1D(self, points, origin):
        distance = 0
        for p in points:
            distance += abs(p-origin)
        return distance
    
    def collect_rows(self, grid):
        rows = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    rows.append(row)
        return rows
    
    def collect_cols(self, grid):
        cols = []
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col]:
                    cols.append(col)
        return cols