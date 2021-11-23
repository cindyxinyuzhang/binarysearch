#max heap
class Solution:
    def solve(self, cells):
        cells = [-cell for cell in cells]
        heapify(cells)

        while len(cells) > 1:
            a, b = -heappop(cells), -heappop(cells)
            if a != b:
                heappush(cells, -floor((a+b)/3))

        return -1 if not cells else -cells[0]
