class Solution(object):
    def getConcatenation(self, nums):
        ans = nums+nums
        return ans
    def containsDuplicate(self, nums):
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
    def runningSum(self, nums):
        sum1 = 0

        for i in range(len(nums)):
            sum1 += nums[i]
            nums[i] = sum1
        return nums
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum += nums[i]
        return -1  