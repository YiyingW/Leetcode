class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []: return 0
        n = len(nums)
        i = 0
        j = n-1
        while (i < j):
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i] == val and nums[j] == val:
                j -= 1
            else:
                i += 1
        if nums[i] == val:
            length = i
            nums = nums[:i-1]
        else:
            length = i + 1
            nums = nums[:i]
        return length
        
        