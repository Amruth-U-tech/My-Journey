class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total-left_sum-nums[i]

            if right_sum==left_sum:
                return i
            left_sum += nums[i]
        return -1
    
    def findDisappearedNumbers(self, nums):
        hashset = set()
        missing = []

        for i in nums:
            if i not in hashset:
                hashset.add(i)
        
        for i in range(1,len(nums)+1):
            if i not in hashset:
                missing.append(i)
        return missing
    def findDisappearedNumbers(self, nums):
        missing = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])

        for i in range(len(nums)):
            if nums[i]>0:
                missing.append(i+1) 
        return missing