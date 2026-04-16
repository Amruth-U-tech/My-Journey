class Solution(object):
    def maxSubArray(self, nums):
        sum_len = 0
        start = 0
        end = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            end+=1
            sum_len = sum(nums[start:end])
            if sum_len<0:
                start = end
            max_sum = max(max_sum,sum_len)
        return max_sum
#optimal code for the above problem
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        current_sum=0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum,current_sum)

            if current_sum<0:
                current_sum = 0
        return max_sum 

    def lengthOfLongestSubstring(self, s):
        
        start = 0
        end = 0
        max_len = 0
        for letter in s:
            
            if letter in s[start:end]:
                start = end
            end += 1
            max_len = max(max_len,len(s[start:end]))
        return max_len  
           