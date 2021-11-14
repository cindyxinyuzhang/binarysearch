class Solution:
    def solve(self, matrix):
        if not matrix: return 0

        seen = set()
        stack = []
        ans = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (r, c) not in seen and matrix[r][c] == 1:
                    seen.add((r,c))
                    ans += 1
                    stack.append((r,c))
                    while stack:
                        r1, c1 = stack.pop()
                        for r2, c2 in [(r1+1, c1), (r1-1, c1), (r1, c1+1), (r1, c1-1)]:
                            if 0 <= r2 < len(matrix) and 0 <= c2 < len(matrix[0]) and matrix[r2][c2] == 1 and (r2,c2) not in seen:
                                stack.append((r2,c2))
                                seen.add((r2,c2))
        return ans
