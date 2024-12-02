class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        i = n - 2
        
        # Step 1: Find the pivot
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        if i >= 0:  # If a pivot was found
            # Step 2: Find the successor
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            
            # Step 3: Swap pivot and successor
            arr[i], arr[j] = arr[j], arr[i]
        
        # Step 4: Reverse the suffix
        arr[i + 1:] = reversed(arr[i + 1:])
        
        return arr
