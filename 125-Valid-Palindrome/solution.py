class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.simplifyString(s)
        if s == '': return True
        for i in range(0, len(s)/2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
        
    def simplifyString(self, s):
        new = []
        for letter in s:
            if ord(letter)>=ord('a') and ord(letter)<=ord('z'):
                new.append(letter)
            elif ord(letter)>=ord('A') and ord(letter)<=ord('Z'):
                chara = chr(ord('a')+ord(letter)-ord('A'))
                new.append(chara)
        newstring=''
        for i in range(0, len(new)):
            newstring += new[i]
        return newstring
        