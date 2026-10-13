class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = [start]
        
        while queue:
            curr = queue.pop(0)
            if arr[curr] == 0:
                return True
            if curr in visited:
                continue
            visited.add(curr)
            
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < len(arr) and next_idx not in visited:
                    queue.append(next_idx)
                    
        return False