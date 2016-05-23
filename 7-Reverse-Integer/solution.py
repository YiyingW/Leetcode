class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x/abs(x)
        return int(str(abs(x))[::-1])*sign