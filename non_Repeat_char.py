
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        MAX_CHAR = 26
        freq = [0] * MAX_CHAR
        
        # Count the frequency of all characters
        for c in s:
            freq[ord(c) - ord('a')] += 1
    
        # Find the first character with frequency 1
        for i in range(len(s)):
            if freq[ord(s[i]) - ord('a')] == 1:
                return s[i]
    
        # If no character is non-repeated, return '$'
        return '$'

