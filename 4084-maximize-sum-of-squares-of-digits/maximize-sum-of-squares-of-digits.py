class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 0 or sum > 9 * num:
            return ""
        
        res = []
        for i in range(num):
            d = min(9, sum)
            res.append(str(d))
            sum -= d
            
        return "".join(res)