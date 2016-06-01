class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strings = str.split(" ")
        if (len(pattern) != len(strings)): return False
        store1={}
        for i in range(0, len(pattern)):
            if pattern[i] not in store1.keys():
                store1[pattern[i]] = strings[i]
            else:
                if store1[pattern[i]] != strings[i]: return False
        store2={}
        for i in range(0, len(strings)):
            if strings[i] not in store2.keys():
                store2[strings[i]] = pattern[i]
            else:
                if store2[strings[i]] != pattern[i]: return False
        return True