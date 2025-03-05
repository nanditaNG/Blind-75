class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        #using a two-pointer approach
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices) and prices[j] > prices[i]:
                if prices[i] < prices[j]:
                    diff = prices[j] - prices[i]
                    maxPrice = max(diff, maxPrice)
                j += 1
        return maxPrice
