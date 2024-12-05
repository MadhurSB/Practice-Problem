class Solution:
    def maximumProfit(self, prices):
        minimum_no = prices[0]
        profit = 0
    
        # Update the minimum value seen so far 
        # if we see smaller
        for i in range(1, len(prices)):
            minimum_no = min(minimum_no, prices[i])
            
            # Update result if we get more profit                
            profit = max(profit, prices[i] - minimum_no)
        
        return profit
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends
