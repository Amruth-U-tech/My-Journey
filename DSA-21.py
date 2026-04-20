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
            
#the issue with the above code is in case like [1,2,3,4,5] with target=11 it fails cause we reset the whole window to zero and start from scratch
'''
my logic:

resets too early
misses shorter valid windows
⚔️ Conceptual Mistake

You are doing:

“expand → hit target → reset”

Correct approach needs:

“expand → shrink → find minimum”'''       

#so tried to shrink the window instead of resetting it completly and found this way
class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_len = float('inf')
        surrent_sum = 0
        current_len = 0
        for end in range(len(nums)):
            surrent_sum += nums[end]
            current_len += 1
            if surrent_sum>=target:
                while surrent_sum>target:
                    surrent_sum -= nums[end-current_len]
                    current_len-=1
                surrent_sum = 0
                min_len = min(min_len,current_len)
                current_len = 0
                
        if min_len==float('inf'):
            return 0
        return min_len
            
        