class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {"(":")", "[":"]","{":"}"}
        stack = []
        for sambol in s:
            if sambol == '(' or sambol == '[' or sambol == '{':
                stack.append(sambol)
            else:
                toppest = stack.pop()
                if toppest not in match.keys(): return False
                if match[toppest] != sambol:
                    return False
        if len(stack) != 0: return False 
        return True
                    
                    
                
    

    