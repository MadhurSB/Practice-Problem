class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # Handle cases where d > n
        # Rotate the array using slicing
        rotated = arr[d:] + arr[:d]
        
        # Modify the original array in place
        for i in range(n):
            arr[i] = rotated[i] 
