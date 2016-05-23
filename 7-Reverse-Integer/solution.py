class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x != 0:
            sign = x/abs(x)
            num = int(str(abs(x))[::-1])
            if num >= 2**31:
                return 0
            else:
                return sign*num
        else:
            return 0