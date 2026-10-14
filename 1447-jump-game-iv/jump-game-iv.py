from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        queue = deque([0])
        visited = {0}
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                if curr == n - 1:
                    return steps
                
                # Check all neighbors: curr + 1, curr - 1, and same values
                neighbors = []
                if curr + 1 < n:
                    neighbors.append(curr + 1)
                if curr - 1 >= 0:
                    neighbors.append(curr - 1)
                
                if arr[curr] in graph:
                    neighbors.extend(graph[arr[curr]])
                    # Clear graph[arr[curr]] to avoid revisiting the same values repeatedly (optimization)
                    del graph[arr[curr]]
                
                for nxt in neighbors:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
                        
            steps += 1
            
        return -1