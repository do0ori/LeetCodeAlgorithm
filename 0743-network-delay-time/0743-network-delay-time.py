class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        # dijkstra
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[0] = dist[k] = 0
        q = [(0, k)]

        while q:
            current_cost, current_node = heapq.heappop(q)

            if dist[current_node] < current_cost: continue

            for next_node, cost in graph[current_node]:
                new_cost = current_cost + cost
                if dist[next_node] > new_cost:
                    dist[next_node] = new_cost
                    heapq.heappush(q, (new_cost, next_node))
        
        result = max(dist)
        return result if result != INF else -1