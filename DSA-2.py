class Solution(object):
    def findErrorNums(self, nums):
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                dup = nums[i]
                if nums[0]>nums[1]:
                    real = nums[i]-1
                else:
                    real = nums[i]+1
                return [dup,real]
nums = [3,2,2]
print(sol.findErrorNums(nums))          