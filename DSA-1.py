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
    def findMaxConsecutiveOnes(self, nums):
        max1 = 0
        iterations = 0
        for i in nums:
            if i==1:
                iterations+=1
            else:
                if max1<iterations:
                    max1=iterations 
                iterations=0
        return(max([iterations,max1]))
        
sol = Solution()
nums = [1,3,2,1]
sol.getConcatenation(nums)