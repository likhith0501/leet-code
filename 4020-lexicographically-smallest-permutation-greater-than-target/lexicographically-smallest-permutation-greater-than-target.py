from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        # Try to find the longest matching prefix of `target`
        # and keep track of character counts remaining.
        prefix_counts = []
        curr_counts = Counter(s_counts)
        matched_until = -1
        
        for i in range(n):
            prefix_counts.append(Counter(curr_counts))
            ch = target[i]
            if curr_counts[ch] > 0:
                curr_counts[ch] -= 1
                matched_until = i
            else:
                break
        
        # Backtrack from the longest possible match to find the rightmost position 
        # where we can place a character strictly greater than target[i]
        for i in range(matched_until + 1, -1, -1):
            if i >= n:
                continue
            
            counts = prefix_counts[i]
            target_char = target[i]
            
            # Find the smallest character available in `counts` strictly greater than `target_char`
            greater_char = None
            for ch in sorted(counts.keys()):
                if ch > target_char and counts[ch] > 0:
                    greater_char = ch
                    break
            
            if greater_char is not None:
                # Build the answer up to index i
                result = list(target[:i]) + [greater_char]
                counts[greater_char] -= 1
                
                # Append remaining characters in sorted order
                for ch in sorted(counts.keys()):
                    result.append(ch * counts[ch])
                
                return "".join(result)
        
        return ""