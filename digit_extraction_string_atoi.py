#User function template for Python
class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        result = 0
        sign = 1
        i = 0
    
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        
        while i < len(s) and '0' <= s[i] <= '9':  
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1
        
        result *= sign
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
