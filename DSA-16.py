class Solution(object):
    def moveZeroes(self, nums):
        index1 = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[index1]=nums[index1],nums[i]
                index1+=1
        return nums
        