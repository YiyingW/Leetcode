class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)[2:].zfill(32)
        new_num = []
        for i in range(len(num)-1, -1, -1):
            new_num.append(num[i])
        return int("".join(new_num), base=2)
        
        
        