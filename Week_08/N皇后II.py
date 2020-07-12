class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1: return []
        count = 0
        def dfs(row, cols, pre, na):
            nonlocal count
            if row >= n:
                count += 1
                return
            bits = (~(cols | pre | na)) & ((1 << n) - 1)

            while bits:
                p = bits & -bits
                bits &= bits - 1
                dfs(row + 1, cols | p, (pre | p) << 1, (na | p) >> 1)
        dfs(0, 0, 0, 0)
        return count