from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        N = len(graph)
        
        # 모든 노드를 방문했을 때의 비트마스크 (N이 4면 1111(2) = 15)
        ALL_VISITED = (1 << N) - 1
        
        # 큐 요소: (현재 노드, 현재까지 방문 상태 비트마스크, 이동 횟수)
        q = deque()
        visited = set()
        
        # 노드가 1개만 있는 예외 케이스 처리
        if N == 1:
            return 0
            
        # 출발점이 어디여도 상관없으므로, 모든 노드를 각각의 출발점으로 큐에 넣음
        for i in range(N):
            mask = 1 << i
            q.append((i, mask, 0))
            visited.add((i, mask))
            
        while q:
            curr, mask, dist = q.popleft()
            
            # 연결된 인접 노드들 탐색
            for neighbor in graph[curr]:
                next_mask = mask | (1 << neighbor)
                
                # 모든 노드를 전부 방문한 순간, 그 거리가 곧 최단 거리!
                if next_mask == ALL_VISITED:
                    return dist + 1
                    
                # 아직 '이 노드에 이 방문 상태'로 도달한 적이 없다면
                if (neighbor, next_mask) not in visited:
                    visited.add((neighbor, next_mask))
                    q.append((neighbor, next_mask, dist + 1))
                    
        return 0