class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        l1 = s1.split(" ")
        l2 = s2.split(" ")
        ret = []
        p = {}
        for n in l1:
            if n not in p:
                p[n] = 1
            else: 
                p[n] += 1
        for n in l2:
            if n not in p:
                p[n] = 1
            else: 
                p[n] += 1
        for k,v in p.items():
            if v == 1:
                ret.append(k)


        return ret
        