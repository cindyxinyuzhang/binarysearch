class Solution:
    def solve(self, matrix):
        n = len(matrix)
        letters = set(matrix[0])
        
        return all(len(set(row))==n and set(row)==letters for row in matrix) and all(len(set(col))==n for col in zip(*matrix))
