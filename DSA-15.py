class Solution(object):
    from collections import defaultdict
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list) 
        #this tell that by default the values of each key is list

        for word in strs:
            encoder = [0]*26
            for letter in word:
                index = ord(letter)-ord('a')
                encoder[index]+=1
            key = tuple(encoder) #key must be immutable
            hashmap[key].append(word) #as default is list u can append directly
        return list(hashmap.values())              

    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1]*n

        for i in range(1,n):
            ans[i]*=nums[i-1]

        right = n-2

        for i in range(n):
            ans[right]*=nums[right+1]
            right-=1
            
        return ans
    
    def maxProfit(self, prices):
        buy_pointer = 0
        sell_pointer = 0
        max_profit = 0

        for i in range(len(prices)):
            
            profit = prices[sell_pointer]-prices[buy_pointer]

            if profit<0 or prices[i]<prices[buy_pointer]:
                buy_pointer=i
            max_profit = max(max_profit,profit)
            sell_pointer+=1
        return max_profit
            