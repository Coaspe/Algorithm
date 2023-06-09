class Solution:
    def minTotalDistance(self, grid):
        rows, cols = [], []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        m_r, m_c = rows[len(rows)//2], cols[len(cols)//2]
        return self.minDistance1D(rows, m_r) + self.minDistance1D(cols, m_c)

    def minDistance1D(self, points, origin):
        distance = 0
        for p in points:
            distance += abs(p-origin)
        return distance