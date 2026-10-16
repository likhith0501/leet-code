class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()
        
        # Insert all prefixes of numbers in arr1 into the set
        for val in arr1:
            s = str(val)
            current = ""
            for char in s:
                current += char
                prefix_set.add(current)
                
        max_len = 0
        
        # Check all prefixes of numbers in arr2 against the set
        for val in arr2:
            s = str(val)
            current = ""
            for char in s:
                current += char
                if current in prefix_set:
                    max_len = max(max_len, len(current))
                    
        return max_len