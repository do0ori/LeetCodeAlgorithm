class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        available = []

        for course in range(numCourses):
            if indegree[course] == 0:
                available.append(course)

        order = []

        while available:
            course = available.pop()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    available.append(next_course)

        return order if len(order) == numCourses else []