class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=prices[0]
        t=0
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            profit=prices[i]-min_price
            if profit>t:
                t=profit
        return t

