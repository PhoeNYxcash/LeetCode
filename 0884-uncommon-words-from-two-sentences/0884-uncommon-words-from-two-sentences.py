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
        freq = Counter(l1 + l2)
        print(freq)
        for k,v in freq.items():
            if v == 1:
                ret.append(k)


        return ret
        