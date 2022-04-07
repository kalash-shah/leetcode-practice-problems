import collections

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = collections.deque()
        opening_brackets = set('([{')
        closing_brackets = set(')]}')
        pair = {')' : '(' , ']' : '[' , '}' : '{'}
        for element in s :
            if element in opening_brackets :
                stack.append(element)
            if element in closing_brackets :
                if not stack :
                   return False 
                elif stack.pop() != pair[element] :
                   return False
                else :
                    continue

        if not stack :
            return True 
        else :
            return False
