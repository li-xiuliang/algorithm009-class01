class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def dfs(queens, xy_sub, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens[:])
                return
            for j in range(n):
                if j not in queens and p - j not in xy_sub and p + j not in xy_sum:
                    queens.append(j)
                    xy_sub.append(p - j)
                    xy_sum.append(p + j)
                    dfs(queens, xy_sub, xy_sum)
                    queens.pop()
                    xy_sub.pop()
                    xy_sum.pop()
        res = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in row] for row in res]