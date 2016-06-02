class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        for i in range(0, len(nums)):
            t[nums[i]] = i
        
        for i in range(0, len(nums)):
            if ((target - nums[i]) in t.keys()):
                if (i!=t[(target - nums[i])]):
                    return [i, t[(target - nums[i])]]