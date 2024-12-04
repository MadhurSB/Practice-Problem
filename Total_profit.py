total_profit = 0

        # Traverse the price list to accumulate profits
        for i in range(1, len(prices)):
            # Add profit if there's an upward trend
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
