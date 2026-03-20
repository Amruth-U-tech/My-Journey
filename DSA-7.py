class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1

    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
    def findDisappearedNumbers(self, nums):
        missing = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])

        for i in range(len(nums)):
            if nums[i]>0:
                missing.append(i+1) 
        return missing

    def maxProfit(self, prices):
        buy = prices[0]
        max1 = 0
        for i in range(len(prices)):
            sell = prices[i]
            if prices[i]<buy:
                buy=prices[i]
            if sell-buy>max1:
                max1 = sell-buy
        return max1
