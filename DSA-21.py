class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_len = float('inf')
        start = 0
        surrent_sum = 0
        current_len = 0
        for end in range(len(nums)):
            surrent_sum += nums[end]
            current_len += 1
            if surrent_sum>=target:
                start = end+1
                min_len = min(min_len,current_len)
                current_len = 0
                surrent_sum = 0
        if min_len==float('inf'):
            return 0
        return min_len
            
            
        