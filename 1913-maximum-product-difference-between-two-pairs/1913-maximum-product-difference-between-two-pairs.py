class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = max(nums)
        c = min(nums)
        nums.remove(max(nums))
        nums.remove(min(nums))
        b = max(nums)
        d = min(nums)
        return (a * b) - (c * d)
