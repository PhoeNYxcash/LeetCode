class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        fact = []
        for i in range(1,n+1):
            num = n % i
            if num == 0:
                fact.append(i)
        print(len(fact))
        if len(fact) == k:
            return fact[k-1]
        elif len(fact) < k:
            return -1
        else:
            return fact[k-1]

        