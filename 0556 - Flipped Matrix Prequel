class Solution:
    def solve(self, matrix):
        row_sums = {}
        col_sums = {}
        total = sum(sum(row) for row in matrix)
        ans = 0
        for r in range(len(matrix)):
            row_sums[r] = sum(matrix[r])
        for c in range(len(matrix[0])):
            col_sums[c] = sum(row[c] for row in matrix)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    new_total = total + (len(matrix[0])-2*row_sums[r]) + (len(matrix)-2*col_sums[c]) - 2
                if matrix[r][c] == 1:
                    new_total = total + (len(matrix[0])-2*row_sums[r]) + (len(matrix)-2*col_sums[c]) + 2
                ans = max(ans, new_total)
        return ans
