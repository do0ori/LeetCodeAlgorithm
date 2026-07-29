import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]

        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        probs = [0] * n
        probs[start_node] = 1
        q = [(-1, 1, start_node)]   # 최대 힙

        while q:
            _, curr_probs, curr_node = heapq.heappop(q)

            if probs[curr_node] > curr_probs: continue

            for nxt_node, prob in graph[curr_node]:
                new_prob = curr_probs * prob

                if probs[nxt_node] < new_prob:
                    probs[nxt_node] = new_prob
                    heapq.heappush(q, (-new_prob, new_prob, nxt_node))
        
        return probs[end_node]