class Solution:
    def solve(self, matrix, blocks):

        block_to_coords = {matrix[r][c] : [r, c] for r in range(len(matrix)) for c in range(len(matrix[0]))}
        ans = 0

        start = [0, 0]

        for block in blocks:
            dest = block_to_coords[block]
            ans += abs(start[0]-dest[0])+abs(start[1]-dest[1])
            start = dest

        return ans
