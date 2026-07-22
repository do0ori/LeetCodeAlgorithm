class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        const int MOD = 1000000007;
        vector<vector<vector<int>>> memo(
            m, vector<vector<int>>(n, vector<int>(maxMove + 1, -1))
        );

        function<int(int, int, int)> dfs = [&](int r, int c, int movesLeft) -> int {
            if (r < 0 || r >= m || c < 0 || c >= n) return 1;
            if (movesLeft == 0) return 0;
            if (memo[r][c][movesLeft] != -1) return memo[r][c][movesLeft];

            long long ans = 0;
            ans += dfs(r + 1, c, movesLeft - 1);
            ans += dfs(r - 1, c, movesLeft - 1);
            ans += dfs(r, c + 1, movesLeft - 1);
            ans += dfs(r, c - 1, movesLeft - 1);

            return memo[r][c][movesLeft] = ans % MOD;
        };

        return dfs(startRow, startColumn, maxMove);
    }
};