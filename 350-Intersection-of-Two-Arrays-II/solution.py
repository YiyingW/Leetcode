class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = {}
        for num in nums1:
            if num not in nums1_dict.keys():
                nums1_dict[num] = 1
            else:
                nums1_dict[num]+=1
        result = []
        for num in nums2:
            if num in nums1_dict.keys() and nums1_dict[num]!= 0:
                result.append(num)
                nums1_dict[num] -= 1
        return result
        