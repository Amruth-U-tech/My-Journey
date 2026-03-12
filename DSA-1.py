class Solution(object):
    def getConcatenation(self, nums):
        if len(nums)>1000 or len(nums)<1:
            return 0
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
sol = Solution()
nums = [1,3,2,1]
sol.getConcatenation(nums)