import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        binary: O(log(N²)) = O(log N)
        
        V = E = N²
        dfs/bfs: O(V + E) = O(N²)

        binary * dfs/bfs = O(N² log N)
        """
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        N = len(grid)
        left, right = 0, N ** 2 - 1

        def can_reach(t):
            if grid[0][0] > t: return False

            visited = [[False] * N for _ in range(N)]
            visited[0][0] = True
            stack = [(0, 0)]

            while stack:
                r, c = stack.pop()

                if r == N - 1 and c == N - 1:
                    return True

                for (dr, dc) in D:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < N and 0 <= nc < N): continue

                    if not visited[nr][nc] and grid[nr][nc] <= t:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
            
            return False

        while left <= right:
            mid = (left + right) // 2

            if can_reach(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
    
    def swimInWater_dijkstra(self, grid: List[List[int]]) -> int:
        """
        V = N²
        E = 4N²
        O(E log V) = O(N² log 4N²) = O(N² log N)
        """
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
