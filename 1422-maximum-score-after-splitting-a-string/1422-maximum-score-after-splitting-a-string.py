class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        for n in range(1,len(s)):
            x = s[:n]
            y = s[n:]
            sx = x.count("0")
            sy = y.count("1")
            if sx + sy > score:
                score = sx + sy
        return score

            
        