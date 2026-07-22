"""
dfs(r, c, movesLeft)
=
dfs(r+1, c, movesLeft-1)
+ dfs(r-1, c, movesLeft-1)
+ dfs(r, c+1, movesLeft-1)
+ dfs(r, c-1, movesLeft-1)

memoization
= dp[r][c][k]: (r, c)에서 movesLeft번 남았을 때 밖으로 나가는 경로 수
"""
from functools import lru_cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(r, c, movesLeft):
            if not (0 <= r < m and 0 <= c < n):
                return 1
            if movesLeft == 0:
                return 0

            return (
                dfs(r + 1, c, movesLeft - 1)
                + dfs(r - 1, c, movesLeft - 1)
                + dfs(r, c + 1, movesLeft - 1)
                + dfs(r, c - 1, movesLeft - 1)
            ) % MOD

        return dfs(startRow, startColumn, maxMove)
        