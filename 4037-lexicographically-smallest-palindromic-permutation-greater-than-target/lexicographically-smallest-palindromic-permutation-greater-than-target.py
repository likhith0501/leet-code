from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # 1. Verify if palindrome can be formed
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = Counter({ch: cnt // 2 for ch, cnt in counts.items()})
        m = n // 2
        
        def build_palindrome(first_half_list):
            first_half = "".join(first_half_list)
            return first_half + mid_char + first_half[::-1]

        best_res = None

        # 2. Try prefix lengths of target[:m] that can be matched exactly
        curr_counts = Counter(half_counts)
        prefix = []
        
        for i in range(m + 1):
            # Attempt A: If we matched target[:i], try making index i strictly greater
            if i < m:
                target_char = target[i]
                for ch in sorted(curr_counts.keys()):
                    if ch > target_char and curr_counts[ch] > 0:
                        # Construct smallest valid continuation
                        rem_counts = Counter(curr_counts)
                        rem_counts[ch] -= 1
                        
                        half_res = prefix + [ch]
                        for r_ch in sorted(rem_counts.keys()):
                            half_res.extend([r_ch] * rem_counts[r_ch])
                        
                        cand = build_palindrome(half_res)
                        if cand > target:
                            if best_res is None or cand < best_res:
                                best_res = cand
                        break # We only need the smallest strictly greater character at index i

            # Attempt B: If we matched up to m (exact match of first half), build full palindrome
            if i == m:
                cand = build_palindrome(prefix)
                if cand > target:
                    if best_res is None or cand < best_res:
                        best_res = cand

            # Advance prefix match for next iteration
            if i < m:
                ch = target[i]
                if curr_counts[ch] > 0:
                    curr_counts[ch] -= 1
                    prefix.append(ch)
                else:
                    break # Cannot match further prefix

        return best_res if best_res is not None else ""