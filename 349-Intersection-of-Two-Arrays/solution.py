class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        check1 = {}
        for num in nums1:
            if num not in check1.keys():
                check1[num] = 1
        intersec = []
        for num in nums2:
            if num in check1.keys():
                intersec.append(num)
                del check1[num]
        return intersec