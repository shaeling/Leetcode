My:
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        vertical = [max(row) for row in grid]
        horizontal = [max(col) for col in zip(*grid)]
        original = 0
        for height in grid:
            original += sum(height)

        extra = 0
        for element in vertical:
            for standard in horizontal:
                if standard > element:
                    extra += standard - element

        return (sum(horizontal) * len(grid) - extra - original)


Offical :

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))