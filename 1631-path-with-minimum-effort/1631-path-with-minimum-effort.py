class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        INF = float('inf')
        N, M = len(heights), len(heights[0])
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        effort = [[INF] * M for _ in range(N)]
        effort[0][0] = 0
        q = [(0, 0, 0)]
        
        while q:
            current_effort, r, c = heapq.heappop(q)

            if effort[r][c] < current_effort: continue

            for dr, dc in D:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < M:
                    next_effort = max(current_effort, abs(heights[nr][nc] - heights[r][c]))

                    if next_effort < effort[nr][nc]:
                        effort[nr][nc] = next_effort
                        heapq.heappush(q, (next_effort, nr, nc))
        
        return effort[N - 1][M - 1]