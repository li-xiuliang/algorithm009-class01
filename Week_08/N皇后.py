class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def solve(pre, xy_sub, xy_sum):
            p = len(pre)
            if p == n:
                res.append(pre)
                return
            for q in range(n):
                if q not in pre and p - q not in xy_sub and p + q not in xy_sum:
                    solve(pre + [q], xy_sub + [p- q], xy_sum + [p + q])
        res = []
        solve([],[],[])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in row] for row in res]