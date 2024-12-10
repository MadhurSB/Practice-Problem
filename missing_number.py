
class Solution:

    # Function to find the smallest positive number missing from the array
    def missingNumber(self, arr):
       
        arr = [num for num in arr if num > 0]
      
        arr_set = set(arr)
       
        num = 1
        while True:
            if num not in arr_set:
                return num
            num += 1
