class Solution(object):
    def getConcatenation(self, nums):
        if len(nums)>1000 or len(nums)<1:
            return 0
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
    def shuffle(self, nums, n):
        l = []
        for i in range(n):
            l.append(nums[i])
            l.append(nums[i+n])
        return l
sol = Solution()
nums = [1,3,2,1]
sol.getConcatenation(nums)