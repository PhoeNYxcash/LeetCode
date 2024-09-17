class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        R = 0
        L = 0
        for n in s:
            if n == 'R':
                R += 1
            else:
                L += 1
            if R == L:
                count += 1
                R =0
                L = 0
        return count


        