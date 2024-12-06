class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0  # If there's only one element, the difference is 0.

        # Sort the array
        arr.sort()

        # Initialize result as the difference between max and min in the original array
        result = arr[-1] - arr[0]

        # Traverse the array and calculate the possible minimum and maximum
        for i in range(1, n):
            if arr[i] >= k:  # Ensure no negative heights
                max_val = max(arr[-1] - k, arr[i - 1] + k)
                min_val = min(arr[0] + k, arr[i] - k)
                result = min(result, max_val - min_val)

        return result
