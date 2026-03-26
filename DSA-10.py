class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
    
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
    def moveZeroes(self, nums):
        v_index = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[v_index],nums[i]=nums[i],nums[v_index]
                v_index+=1
            else:
                continue
        return nums