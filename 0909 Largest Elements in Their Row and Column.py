class Solution:
    def solve(self, matrix):
        row_sums = [sum(row) for row in matrix]
        col_sums = [sum(col) for col in zip(*matrix)]

        return sum(matrix[r][c]==1 for r in range(len(matrix)) for c in range(len(matrix[0]))if row_sums[r]==col_sums[c]==1)
