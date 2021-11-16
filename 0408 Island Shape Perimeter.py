class Solution:
    def solve(self, matrix):
        perimeter = 0
        for R in range(len(matrix)):
            for C in range(len(matrix[0])):
                if matrix[R][C] == 1:
                    for r, c in [[R+1, C], [R-1, C], [R, C+1], [R, C-1]]:
                        if r<0 or r>=len(matrix) or c<0 or c>=len(matrix[0]):
                            perimeter += 1
                        elif matrix[r][c] == 0:
                            perimeter += 1
        return perimeter
