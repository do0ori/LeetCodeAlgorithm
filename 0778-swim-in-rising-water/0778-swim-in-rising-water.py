import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N = len(grid)
        
        times = [[N ** 2 - 1] * N for _ in range(N)]
        times[0][0] = grid[0][0]
        q = [(grid[0][0], 0, 0)]

        while q:
            curr_t, r, c = heapq.heappop(q)

            if times[r][c] < curr_t: continue

            for (dr, dc) in D:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N): continue

                next_t = max(curr_t, grid[nr][nc])
                if times[nr][nc] > next_t:
                    times[nr][nc] = next_t
                    heapq.heappush(q, (next_t, nr, nc))
        
        return times[N - 1][N - 1]
