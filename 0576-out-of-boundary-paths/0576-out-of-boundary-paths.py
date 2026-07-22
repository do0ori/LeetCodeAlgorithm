"""
dfs(r, c, movesLeft)
=
dfs(r+1, c, movesLeft-1)
+ dfs(r-1, c, movesLeft-1)
+ dfs(r, c+1, movesLeft-1)
+ dfs(r, c-1, movesLeft-1)

memoization
= dp[r][c][k]: (r, c)에서 k번 이내로 밖으로 나가는 경로 수
"""
from functools import lru_cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(r, c, movesLeft):
            if r > m - 1 or r < 0 or c > n - 1 or c < 0: return 1
            if movesLeft == 0: return 0
            return (dfs(r + 1, c, movesLeft - 1) + dfs(r - 1, c, movesLeft - 1) + dfs(r, c + 1, movesLeft - 1) + dfs(r, c - 1, movesLeft - 1)) % (10 ** 9 + 7)

        return dfs(startRow, startColumn, maxMove)
        