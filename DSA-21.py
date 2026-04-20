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
    
#the above code is 85% there the issue here is 
# 1.very messy and confusing
# 2.end-current_len part is mimicking start pointer but it can get logically wrong
# 3.window again is resetting which works for some cases but contradictory to others
# ----------hence final clean optimal code is------------

class Solution(object):
    def minSubArrayLen(self, target, nums):
        start = 0
        current_sum = 0
        min_len = float('inf')

        for end in range(len(nums)):
            current_sum += nums[end]

            while current_sum >= target:
                min_len = min(min_len, end - start + 1)
                current_sum -= nums[start]
                start += 1

        return 0 if min_len == float('inf') else min_len            
        