class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = len(prices)
        max_profit = 0
        left,right =0,1
        while right < price:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit= max(profit,max_profit)
            else:
                left = right
            right+=1
        return max_profit

            

