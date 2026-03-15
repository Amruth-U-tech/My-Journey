class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return (n*(n+1))/2 - sum(nums)
class BestTimeToBuyStock(object):
    def maxProfit(self, prices):
        buy = prices[0]
        sell = 0
        max = 0
        for i in prices:
            sell = i
            if i<buy:
                buy = i
            if sell-buy>max:
                max = sell-buy
        return max