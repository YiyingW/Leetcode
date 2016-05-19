class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sum = {}
        self.sum[(0, 0)] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.sum[(0, i)] = self.sum[(0, i-1)] + self.nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.sum[(0, j)] - self.sum[(0, i)]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)