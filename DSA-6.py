class Solution(object):
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
        