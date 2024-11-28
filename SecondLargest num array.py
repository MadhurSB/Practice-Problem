#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
         
        largest = -1
        Second_largest = -1
        
        
        for i in range(n):
            if arr[i] > largest:
                Second_largest = largest
                largest = arr[i]
                
            elif arr[i]<largest and arr[i]>Second_largest:
                Second_largest = arr[i]
            
        return Second_largest
            
