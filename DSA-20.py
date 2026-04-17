class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1])>=1 and nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
            if nums[i]-nums[i+1]==0:
                if abs(nums[i]-nums[i+2])>=1 and nums[i]>nums[i+2]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums