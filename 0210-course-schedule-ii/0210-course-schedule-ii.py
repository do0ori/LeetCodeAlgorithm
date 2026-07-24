class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for [a, b] in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        
        answer = []
        while stack:
            c = stack.pop()
            answer.append(c)
            
            for nxt in graph[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    stack.append(nxt)
        
        if len(answer) < numCourses: return []
        else: return answer